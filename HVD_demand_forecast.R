
library(plyr)
library(forecast)
library(xts)
library(caret)
setwd("C:/Users/a585479/Documents/HVD Demand")

df  = read.csv("SNOW Data_All Time.csv", header = TRUE)

# Split By Week

short.date <- strftime(as.Date(df$Created, format="%m/%d/%Y"), "%Y/%U")

df2 <- aggregate(Number ~ short.date, df, FUN = function(x){NROW(x)})

hvd <- ts(df2$Number,  start=c(2015, 33), end=c(2017, 08), frequency=53)

plot(hvd)

plot(forecast(hvd))
plot(ses(hvd))
attributes(ses(hvd)) # 'forecast' class attributes

# Divide into train and test

hvd_train <- window(hvd, end = c(2017, 06))
hvd_test <- window(hvd, start = c(2017, 07))

# Forecasting using Arima

fit <- auto.arima(hvd, seasonal = FALSE)

fcast <- forecast(fit, h=8)
plot(fcast)
accuracy(fcast, hvd_test)


# Include new variables: Agents moving in and out and HVD count

DF  <- read.csv("People_data.csv", header = TRUE)
DF_2 <- read.csv("HVD_Adoption_data.csv", header = TRUE)

DF['yr_wk'] <- as.POSIXct(paste0(DF$Year, " ", DF$Week, " 1"), format = "%Y %U %u")
DF_2['yr-wk'] <- as.POSIXct(paste0(DF_2$Year, " ", DF_2$Week, " 1"), format = "%Y %U %u") 

xreg <- DF[,3:4]
xreg_2 <- DF_2[,3:4]

people_out <- ts(xreg$People_out, start=c(2015, 33), end=c(2017, 08), frequency = 53)
people_in <- ts(xreg$People_in, start=c(2015, 33), end=c(2017, 08), frequency = 53)

hvd_use <- ts(xreg_2$In_use, start=c(2015, 33), end=c(2017, 08), frequency = 53)
hvd_idle <- ts(xreg_2$Idle, start=c(2015, 33), end=c(2017, 08), frequency = 53)
  
fit_peoplein <- auto.arima(people_in)
fcast_peoplein <- forecast(fit_peoplein, h=8)

fit_peopleout <- auto.arima(people_out)
fcast_peopleout <- forecast(fit_peopleout, h=8)

fit_hvd_use <- auto.arima(hvd_use)
fcast_hvd_use <- forecast(fit_hvd_use, h=8)

fit_hvd_idle <- auto.arima(hvd_idle)
fcast_hvd_idle <- forecast(fit_hvd_idle, h=8)


plot(fcast_peoplein)
plot(fcast_peopleout)

plot(fcast_hvd_use)
plot(fcast_hvd_idle)

#ARIMAX model

xreg_combined <- cbind(xreg,xreg_2)

fit_arimax <- auto.arima(hvd, xreg = xreg_combined)

# Forecasting covariates and the test data
People_out= summary(fcast_peopleout)
People_in = summary(fcast_peoplein)

HVD_in_use = summary(fcast_hvd_use)
HVD_idle = summary(fcast_hvd_idle)

xregnew = as.matrix(cbind(People_out[,1],People_in[,1],HVD_in_use[,1], HVD_idle[,1]))

fcast_arimax <- forecast(fit_arimax, h=8, xreg = xregnew)
plot(fcast_arimax)


