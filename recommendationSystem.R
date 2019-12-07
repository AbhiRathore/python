## recommendation system - collaborative filtering
## set working directory and set seed
set.seed(1111)
setwd("D:/tesseract/goodbooks-10k-master/goodbooks-10k-master/")

## import libraries
library(data.table)
library(dplyr)
library(ggplot2)

## reading data
booksdata=fread("books.csv")
book_tag=fread("book_tags.csv")
tags=fread("tags.csv")
ratings=fread("ratings.csv")

head(booksdata)
head(book_tag)
head(tags)
head(ratings)


length(unique(tags$tag_name))
head(tags,10)

genre_list=c('comedy','thriller','romantic')

tags$tags2=lapply(tags$tag_name,function(x){gsub("[^a-zA-Z]",NA,x)})
head(tags)

tagsfile2=tags[which(is.na(tags$tags2) == F),]

tagsfile2 %>% filter("romantic" %in% tagsfile2$tags2)

tag_genre=list()
for(i in c(1:length(genre_list))) {
q=subset(tagsfile2,tagsfile2$tags2==genre_list[i])
print(q$tags2[[1]][1])
tag_genre[i]=q$tag_id[[1]]
}

### 3 genres selected


book_tag_needed=book_tag %>% filter(book_tag$tag_id %in% tag_genre)

dim(book_tag_needed)
head(book_tag_needed)

ratings_needed=ratings %>% filter(ratings$book_id %in% book_tag_needed$goodreads_book_id)
head(ratings_needed)
dim(ratings_needed)

ratings_needed=ratings_needed %>% filter(ratings_needed$rating >3)


user_count=ratings_needed %>% group_by(book_id) %>% summarise(usercount = n())
dim(user_count)
head(user_count)

barplot(height = user_count$usercount)


p<-ggplot(data=user_count, aes(x=factor(book_id), y=log(usercount))) +
  geom_bar(stat="identity")
p


reserveduser=c(2,4)

reservebook=c(26,27,24,8)


ratings_needed_train=ratings_needed %>% filter(!ratings_needed$book_id %in% reservebook)
ratings_needed_test=ratings_needed %>% filter(ratings_needed$book_id %in% reservebook)

head(ratings_needed_train)
head(ratings_needed_test)

dim(ratings_needed)
length(unique(ratings_needed$user_id))
length(unique(ratings_needed$book_id))


## recommendation engine 

head(ratings_needed)

r <- as(ratings_needed,"realRatingMatrix")
b=as(r, "matrix")

dim(b)
b[1:5,1:50]
as(data_test,'data.frame')
as(data_test,'matrix')
dim(r)
data_train <- r[1:20000]
data_test <- r[20003:20005]

# Find top 10 recomm movies with Item based collab filter
#IBCF
model1 <- Recommender(data = data_train, method = "IBCF", parameter = list(k = 25, 
                                                                        method = "pearson"))
model1

# Applying model to test

predicted1 <- predict(object = model1, newdata = data_test, n = 7)
predicted1

predicted1@items
# The latest among those predicted for each user as most recommended

#reccom <- data.frame(user_id= sort(rep(1:length(predicted1@items))),
#                     rating = unlist(predicted1@ratings), book_id = unlist(predicted1@items))

#Displaying the recommendations for first 25 users

e=lapply(colnames(data.frame(predicted1@items)),function(x){gsub("X","",x)})
e=unlist(e)

#user_test=unique(as(data_test,'data.frame')$user)
reccom <- data.frame(user_id= as.numeric(e),
                     rating = unlist(predicted1@ratings), book_id = unlist(predicted1@items))

reccom_list<- reccom[order(reccom$user_id),] 
head(reccom_list,25)

#subset(reccom_list,reccom_list$user_id %in% c(1083))


filterdata=subset(ratings_needed,ratings_needed$user_id %in% c(1083))
left_join(filterdata,booksdata[,c("book_id","title")],by='book_id')

#filterdata=booksdata %>% filter(booksdata$book_id %in% c(1) ) %>% select(title)


## adding title
left_join(reccom_list,booksdata[,c("book_id","title")],by='book_id') %>% filter(user_id %in% c(1083))


##### adding new data

#ratings_needed$book_id
#c(8,11,13)
testn=data.frame(user_id=c(199911),book_id=sort(unique(ratings_needed$book_id)),rating=NA)
head(testn,50)

testn$rating = ifelse(testn$book_id == 8,4,testn$rating)
testn$rating = ifelse(testn$book_id == 11,5,testn$rating)
testn$rating = ifelse(testn$book_id == 13,5,testn$rating)

testn2 <- as(testn,"realRatingMatrix")
dim(testn2)
dim(data_test)
data_test[1]
predicted2 <- predict(object = model1, newdata = data_test[1], n = 7)
predicted2 <- predict(object = model1, newdata = testn2[1], n = 7)

predicted2
predicted2@items

e2=lapply(colnames(data.frame(predicted2@items)),function(x){gsub("X","",x)})
e2=unlist(e2)

#user_test=unique(as(data_test,'data.frame')$user)
reccom2 <- data.frame(user_id= as.numeric(e2),
                     rating = unlist(predicted2@ratings), book_id = unlist(predicted2@items))

reccom_list2<- reccom2[order(reccom2$user_id),] 
head(reccom_list,25)

#subset(reccom_list,reccom_list$user_id %in% c(1083))


filterdata=subset(ratings_needed,ratings_needed$user_id %in% c(1083))
left_join(filterdata,booksdata[,c("book_id","title")],by='book_id')












########## sample

library("recommenderlab")
data("MovieLense")
### use only users with more than 100 ratings
MovieLense100 <- MovieLense[rowCounts(MovieLense) >100,]
MovieLense100

train <- MovieLense100[1:5,1:5]

b=as(train, "matrix")
dim(b)
b


train <- MovieLense100[1:5,1:50]
rec <- Recommender(train, method = "UBCF")
rec

pre <- predict(rec, MovieLense100[101:102,1:50], n = 10)
pre

as(pre, "list")

####################
## create a matrix with ratings
m <- matrix(sample(c(NA,0:5),100, replace=TRUE, prob=c(.7,rep(.3/6,6))),
            nrow=10, ncol=10, dimnames = list(
              user=paste('u', 1:10, sep=''),
              item=paste('i', 1:10, sep='')
            ))
m

## coerce into a realRatingMAtrix
r <- as(m, "realRatingMatrix")
r

head(ratings_needed_train)

r <- as(ratings_needed_train,"realRatingMatrix")

r <- as(m, "realRatingMatrix")
r

## get some information
dimnames(r)
rowCounts(r) ## number of ratings per user
colCounts(r) ## number of ratings per item
colMeans(r) ## average item rating


## histogram of ratings
hist(getRatings(r), breaks="FD")

## inspect a subset
image(r[1:5,1:5])

## coerce it back to see if it worked
as(r, "matrix")

## coerce to data.frame (user/item/rating triplets)
head(as(r, "data.frame"))

## binarize into a binaryRatingMatrix with all 4+ rating a 1
b <- binarize(r, minRating=4)
b
as(b, "matrix")


######
library(recommenderlab)

#Convert data.frame in to transactions:
#Convert to binaryRatingMatrix:

m <- matrix(sample(c(0,1), 50, replace=TRUE), nrow=5, ncol=10,
            dimnames=list(users=paste("u", 1:5, sep=''),
                          items=paste("i", 1:10, sep='')))
m

b <- as(m, "binaryRatingMatrix")
b
as(b, "matrix")

dim(ratings_needed_test)
dim(ratings_needed_train)
