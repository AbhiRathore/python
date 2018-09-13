set.seed(100)
library(dplyr)
library(ggplot2)
library(e1071)
library(dummies)
library(data.table)
library(DMwR)
library(caTools)
library(xgboost)
library(caret)

library(tm)
library(tibble)

setwd("E:/wns_AV/")

train=read.csv("train.csv",header = T,na.strings = c("na",NA,"null"))
test=read.csv("test.csv",header = T,na.strings = c("na",NA,"null"))
names(train)
names(test)
test$is_promoted=0
totalData=rbind(train,test)
head(totalData)

totalData <- dummy.data.frame(totalData,names=c("department","region",'education','gender','recruitment_channel'), sep="_")


## 
train=totalData[c(1: 54808),]
test=totalData[c(54809: nrow(totalData)),]

split<-sample.split(train$is_promoted,SplitRatio = 0.8)
train2=subset(train,split==TRUE)
val=subset(train,split==FALSE)

for (i in c(2:60)){
  train2[,i] = as.numeric(train2[,i])
}

str(train2)

#X_features=c("perc_premium_paid_by_cash_credit","age_in_days","Count_3.6_months_late","Count_6.12_months_late",       
#             "Count_more_than_12_months_late","application_underwriting_score","no_of_premiums_paid",
#             "sourcing_channel_A","sourcing_channel_B","sourcing_channel_C",           
#             "sourcing_channel_D","sourcing_channel_E","residence_area_type_Rural",
#             "residence_area_type_Urban","premium","permiumLeft",
#             "Income2_high","Income2_low","Income2_med")

#X_target <- as.numeric(train2$is_promoted)-1

X_target=train2$is_promoted

## xgboost
model_xgb_cv <- xgb.cv(data=as.matrix(train2[, c(2:60)]), label=as.matrix(X_target), nfold=20, 
                       objective="binary:logistic", nrounds=800, eta=0.005, max_depth=10, 
                       subsample=0.75, colsample_bytree=0.8, min_child_weight=1, eval_metric="auc")


model_xgb <- xgboost(data=as.matrix(train2[, c(2:60)]),label=as.matrix(X_target), 
                      objective="binary:logistic", nrounds=600, eta=0.005, max_depth=10, subsample=0.75, 
                      colsample_bytree=0.7, min_child_weight=2, eval_metric="auc")

g=names(train2)
X_features = g[2:60]

vimp <- xgb.importance(model = model_xgb, feature_names = X_features)
View(vimp)
for (i in c(2:60)){
  val[,i] = as.numeric(val[,i])
}

pred <- predict(model_xgb, as.matrix(val[, c(2:60)]))

plot(pred)
pred2=factor(ifelse(pred>.1,1,0))

confusionMatrix(data = pred2,reference = val$is_promoted,positive = '1')



####### test data
for (i in c(2:60)){
  test[,i] = as.numeric(test[,i])
}


pred3 <- predict(model_xgb, as.matrix(test[, c(2:60)]))
pred4=factor(ifelse(pred3>.1,1,0))

#test$is_promoted=pred3

sub1=data.frame(employee_id=test$employee_id,is_promoted=pred4)
head(sub1)
#names(test)=c('employee_id','is_promoted')

write.csv(sub1,'sub1.csv',row.names = F)





################## reference


train2=total3[1:nrow(train),]
test2=total3[348979:nrow(total3),]

library(corrplot)

corrplot(cor(total3),method = 'number')

memory.size(1233444)

param <- list(booster = "gbtree",
              objective = "binary:logistic",
              eval_metric = "auc",
              #num_class = 9,
              eta = .08,
              # gamma = 1,
              max_depth = 10,
              min_child_weight = 1,
              subsample = .8,
              colsample_bytree = .3)
#



dtrain <- xgb.DMatrix(data = as.matrix(train2[,-c('target','transaction_id'),with=F]), label = (as.integer(train2$target)))
dtest <- xgb.DMatrix(data = as.matrix(test2[,-c('transaction_id','target')]))

cv.model <- xgb.cv(params = param
                   ,data = dtrain
                   ,nrounds = 1000
                   ,nfold = 5L
                   ,stratified = T
                   ,early_stopping_rounds = 40
                   ,print_every_n = 50
                   ,maximize = F)

best_it <- cv.model$best_iteration
best_score <- cv.model$evaluation_log$test_error_mean[which.min(cv.model$evaluation_log$test_error_mean)]

tr.model <- xgb.train(params = param
                      ,data = dtrain
                      ,nrounds = best_it
                      ,watchlist = list(train = dtrain)
                      ,print_every_n = 50)

preds <- predict(tr.model, dtest)
predictions <- ifelse(preds>.4,1,0)
sub1 <- data.table(transaction_id = test2$transaction_id, target = preds)
write.csv(sub1,"sub1.csv",row.names = F)

names(sub1)







