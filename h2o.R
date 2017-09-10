data(iris)
dat=iris[,c(1,2)]
colnames(dat)[1]<-"len"
colnames(dat)[2]<-"wid"
dat$target<-factor(ifelse(dat$len<4.50,1,0))

summary(dat)
