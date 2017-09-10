#####
library(twitteR)
####### give key and  access_secret
consumer_key<-'..........'
consumer_secret<-'.......'
access_token<-'......'
access_secret<-'.........'
li
setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)
#### write yes or no 
##### mining use any one of following whatever suits, recent will tell only recent tweets and by giving date one can get all tweets from that date
trial_1<-searchTwitter("@Honda",n="5000",lan="en",resultType = "recent")
trial_1<-searchTwitter("@Honda",n="500",lan="en",since = "2010-07-07")
#trial_1
class(trial_1) 
#creating text 
trial_txt<-sapply(trial_1,function(x) x$getText())
head(trial_txt)
tweets<-data.frame(trial_txt)
tweets$id<-1:nrow(tweets)
head(tweets)
######## writing in table/csv
tweets2<-data.frame(tweets$id,tweets$trial_txt)
head(tweets2)
### changing column names
colnames(tweets2)[which(names(tweets2) == "  tweets.id")] <- "Id"
colnames(tweets2)[which(names(tweets2) == "tweets.trial_txt")] <- "Tweets_text"
write.csv(tweets2,"tweets.csv",row.names = F)
