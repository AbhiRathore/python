library(ggmap) 
#install.packages("ggmap") # install it if not there already
rm(hdfc) # removing variable , it will show warning if not present, that is file
## step 1 give file location
hdfc=read.csv("D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/pin_geo.csv",header=T)
head(hdfc) # to see top rows
names(hdfc) # to see column names
nrow(hdfc) # to get the count of number of rows
hdfc2=hdfc # copying it
hdfc$address=as.character(hdfc2$address) # to make address as character
# to select limited number of rows as 2500 is the daily limit
####################################################################
nrow(hdfc)
hdfc1=hdfc[1:2400,]
hdfc2=hdfc[2401:3400,]
hdfc3=hdfc[3401:5900,]
hdfc4=hdfc[5901:nrow(hdfc),]
# writing in different file is another machine is to be used
write.csv(hdfc2,"D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/akshita_3july.csv",row.names = F)
## finding lat lon
all.stations=hdfc$address
all.longitudes <- as.numeric(NA[1:length(all.stations)])  
all.latitudes <- as.numeric(NA[1:length(all.stations)])
for ( i  in 1: length(all.stations)) 
{ 
  coordinates <- geocode(all.stations[i]) 
  all.longitudes[i] <- coordinates$lon
  all.latitudes[i] <- coordinates$lat
}
#nrow(all.longitudes)
rm(all.locations3)
all.locations3 <- as.data.frame(cbind(name=all.stations, 
                                     lon=all.longitudes, lat=all.latitudes),
                               stringsAsFactors=FALSE) 
head(all.locations3)
nrow(all.locations3)
rm(all.locations)
#names(hdfc)
all.locations=cbind(hdfc$sn,all.locations3)

#table(is.na(all.locations))
write.csv(all.locations,"D:/a/hdfc_lot1.csv",row.names = F)

