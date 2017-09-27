
write.csv(tweets2,"tweets.csv",row.names = F)
str(trial_txt)##text mining
library(tm)
library(sentiment)
#####
library(twitteR)
library(RCurl)
library(wordcloud)
library(SnowballC) 
library(ggplot2)
#######
consumer_key=''
consumer_secret=''
access_token=''
access_secret=''
setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)
#####mining
trial_1<-searchTwitter("@sachin",n="5000",lan="en",resultType = "recent")
trial_1<-searchTwitter("sachin",n="5000",lan="en",since = "2001-07-07")
#trial_1
class(trial_1) # now class is list hence it is needed to convert into character to make corpus
#creating character vector
trial_txt<-sapply(trial_1,function(x) x$getText())
head(trial_txt)
tweets<-data.frame(trial_txt)
tweets$id<-1:nrow(tweets)
tweets2<-data.frame(tweets$id,tweets$trial_txt)
head(tweets2)
#colnames(trial)<-"tweets"
write.table(tweets2,"tweets",row.names = F)
### changing column names
colnames(tweets2)[which(names(tweets2) == "  tweets.id")] <- "Id"
colnames(tweets2)[which(names(tweets2) == "tweets.trial_txt")] <- "Tweets_text"
class(trial_txt)#now its character

##making corpus
trial_cor<-Corpus(VectorSource(trial_txt))
#trial_cor

####cleaning and treatment
# Convert to lower-case

trial_cor = tm_map(trial_cor, content_transformer(tolower))
x<- c("the world is white")
x
gsub(stopwords("english"),"",x)
stopwords()
trial_cor = tm_map(trial_cor, removePunctuation)
trial_cor= tm_map(trial_cor, removeWords, c("the", stopwords("english")))
trial_cor = tm_map(trial_cor, stripWhitespace)
trial_cor = tm_map(trial_cor, stemDocument)
trial_cor = tm_map(trial_cor, PlainTextDocument)

wordcloud(trial_cor,max.words=Inf,scale = c(5,0.7),random.order=T,use.r.layout=FALSE, rot.per=0.2,color=brewer.pal(8,"Dark2"),random.color=TRUE)


frequencies = DocumentTermMatrix(trial_cor)
inspect(frequencies[1:5,1:20])
###transpose
##frequencies<=TermDocumentMatrix(frequencies)

freq<-colSums(as.matrix(frequencies))
length(freq)
order(freq)
m<-as.matrix(frequencies)
write.csv(m,"freq.csv")
#######

tmf<-removeSparseTerms(frequencies,0.1)
inspect(tmf)
class(trial_txt)
#####

######################################################################################
#####sentiment analysis
#prepare the text for sentiment analysis
# remove retweet entities

trial_txt = gsub("(RT|via)((?:\\b\\W*@\\w+)+)", "", trial_txt)
# remove at people
trial_txt = gsub("@\\w+", "", trial_txt)
# remove punctuation
trial_txt = gsub("[[:punct:]]", "", trial_txt)
# remove numbers
trial_txt = gsub("[[:digit:]]", "", trial_txt)
# remove html links
trial_txt = gsub("http\\w+", "", trial_txt)
# remove unnecessary spaces
trial_txt = gsub("[ \t]{2,}", "", trial_txt)
trial_txt = gsub("^\\s+|\\s+$", "", trial_txt)
head(trial_txt)
# define "tolower error handling" function 
x<- " What a story\njust awesomeMovie\nWatching Mohenjo Daro????????????????????????????????????????????????????????????????????????"


x1<-gsub("[^a-z A-Z0-9 \\\n]","",x)
x1
gsub("\n"," ",x1)
trial_txt<-gsub("[^a-z A-Z0-9\\\n]","",trial_txt)
head(trial_txt)
trial_txt<-gsub("\n"," ",trial_txt)

try.error = function(x)
{
  # create missing value
  y = NA
  # tryCatch error
  try_error = tryCatch(tolower(x), error=function(e) e)
  # if not an error
  if (!inherits(try_error, "error"))
    y = tolower(x)
  # result
  return(y)
}
# lower case using try.error with sapply 
trial_txt = sapply(trial_txt, try.error)

# remove NAs in trial_txt
trial_txt = trial_txt[!is.na(trial_txt)]
head(trial_txt)
names(trial_txt) = NULL
trial_txt<-gsub("[^a-z A-Z0-9]","",trial_txt)
######
##Perform Sentiment Analysis
# classify emotion
class_emo = classify_emotion(trial_txt, algorithm="bayes", prior=1.0)
# get emotion best fit
emotion = class_emo[,7]
head(emotion)
# substitute NA's by "unknown"
emotion[is.na(emotion)] = "unknown"

# classify polarity
class_pol = classify_polarity(trial_txt, algorithm="bayes")
# get polarity best fit

polarity = class_pol[,4]

#head(class_pol)
#Step 5: Create data frame with the results and obtain some general statistics
# data frame with results
sent_df = data.frame(text=trial_txt, emotion=emotion,
                     polarity=polarity, stringsAsFactors=FALSE)
#####
# sort data frame
sent_df = within(sent_df,
                 emotion <- factor(emotion, levels=names(sort(table(emotion), decreasing=TRUE))))
###########
#Let's do some plots of the obtained results
# plot distribution of emotions
ggplot(sent_df, aes(x=emotion)) +
  geom_bar(aes(y=..count.., fill=emotion)) +
  scale_fill_brewer(palette="Dark2") +
  labs(x="emotion categories", y="number of tweets") +
  ggtitle("Sentiment Analysis of Tweets\n(classification by emotion")


# plot distribution of polarity
ggplot(sent_df, aes(x=polarity)) +
  geom_bar(aes(y=..count.., fill=polarity)) +
  scale_fill_brewer(palette="RdGy") +
  labs(x="polarity categories", y="number of tweets") +
  ggtitle("Sentiment Analysis of Tweets\n(classification by polarity)")
###plot.title = theme_text(size=12))

###
#Separate the text by emotions and visualize the words with a comparison cloud
# separating text by emotion
emos = levels(factor(sent_df$emotion))
nemo = length(emos)
emos
emo.docs = rep("", nemo)
head(emo.docs)
names(emo.docs)
for (i in 1:nemo)
{
  tmp = trial_txt[emotion == emos[i]]
  emo.docs[i] = paste(tmp, collapse=" ")
}

# remove stopwords
emo.docs = removeWords(emo.docs, stopwords("english"))
head(emo.docs,1)
# create corpus
library(tm)
corpus_trial = Corpus(VectorSource(emo.docs))
corpus_trial = tm_map(corpus_trial,removeWords,c("the", stopwords("english")))
corpus_trial<-tm_map(corpus_trial,tolower)
tdm_trial = TermDocumentMatrix(corpus_trial)
tdm_trial = as.matrix(tdm_trial)
colnames(tdm_trial) = emos
head(tdm_trial)
# comparison word cloud
windows()
comparison.cloud(tdm_trial, max.words=Inf,colors = brewer.pal(nemo, "Paired"),
                 scale = c(1.5,.3), random.order = FALSE, title.size = 1.5)
dev.off()
#######to pdf
pdf("CarriersCompCloud1.pdf", width=10, height=10)
comparison.cloud(tdm_trial, random.order=FALSE, 
                 colors = c("#00B2FF", "red", "#FF0099", "#6600CC"),
                 title.size=1.5, max.words=10000)
dev.off()
###########pdf2
getwd()
pdf("CompCloud.pdf", width=8, height=8)
comparison.cloud(tdm_trial, random.order=FALSE, 
                 colors = brewer.pal(nemo, "Dark2"),
                 title.size=1.2, max.words=Inf)
dev.off()
############
pdf("Cloud.pdf",width= 10,height=10)
comparison.cloud(tdm_trial, max.words=Inf,colors = brewer.pal(nemo, "Dark2"),
                 scale = c(2,.5), random.order = FALSE, title.size = 1.5)
dev.off()
#######to pdf


########random
dtms <- removeSparseTerms(tdm_trial, 0.1) # This makes a matrix that is 10% empty space, maximum.   
inspect(dtms)  
freq <- colSums(as.matrix(tdm_trial))   
length(freq)   

head(freq)
View(tweets)

head(trial_txt)
head(sent_df)
#############

length(trial_txt)

emo.docs2 = rep("", length(trial_txt))
head(emo.docs2)


#names(emo.docs)
for (i in 1:length(trial_txt))
{
  tmp = trial_txt[i]
  emo.docs2[i] = paste(tmp, collapse=" ")
}
head(emo.docs)
corpus_trial2 = Corpus(VectorSource(emo.docs2))
termf=DocumentTermMatrix(corpus_trial2)
termf
inspect(termf[1:3,])
mytdm=TermDocumentMatrix(corpus_trial2)
inspect(mytdm[1:4,1:4])
findFreqTerms(mytdm, lowfreq=10)
library(wordcloud)
m <- as.matrix(mytdm)
# calculate the frequency of words
v <- sort(rowSums(m), decreasing=TRUE)
myNames <- names(v)

d <- data.frame(word=myNames, freq=v)
wordcloud(d$word, d$freq, min.freq=3)


TW="KOLLEO;2017-07-13 14:55;1;3;"#DeMonetisation failed #SaveIndia #FakeBJPCampaign #fakeBJP #BJPFake #BJPLies DM took 100+ lives"
setwd("D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/")
file2=read.csv("output_got.csv",header = F)
View(file2)
names(file2)<-c("var1","var2")
file3=file2[-1,]
head(file3)
file3$var1<-gsub(pattern = "[^a-z A_Z 0-9 \\,/.;]","",file3$var1)
tw=file3[1,1]
tw
substr(tw,regexpr("https//twitter.com/",tw)[1]+19,regexpr("/status/",tw)[1]-1)





