data(airquality)
data(iris)
names(iris)
tail(iris,10)
nrow(iris)
View(iris)
View(airquality)
names(airquality)
str(airquality)
sapply(cps,function(x){sum(is.na(x))})
str(airquality)
rnorm(2)*5000
k<-0
round(runif(5,5000,500000))
attach(airquality)
557+921+69+331+41+143+9+1344+73+93+24+206+34+422+11+218+59+221+34
coplot(Ozone~Solar.R|Wind,panel=panel.smooth,airquality)
plot(Ozone~Solar.R,airquality)
mean.Temp=mean(airquality$Temp,na.rm=T)
abline(h=mean.Temp)
model<-lm(Ozone~.,data=airquality)
model
data()

summary(model)
pdf("plot.pdf")
anova(model)
termplot(model)

d=subset(airquality,Wind >=9 & Wind <=12)
head(d)
d
plot(Ozone~Solar.R,d)


j=list(c(1,2,3,4),c("asy","dss","sds"))
str(j)
j[[2]][3]
