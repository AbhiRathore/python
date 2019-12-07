setwd("D:/tesseract/") # set working directory
nips_Data=read.csv('NIPS_1987-2015.csv')
dim(nips_Data)
head(nips_Data)
#nips_Data[c(1:nrow(nips_Data)),c(2:10)]

colnames(nips_Data)[colSums(is.na(nips_Data)) > 0]
x=nips_Data[c(1:nrow(nips_Data)),c(2:10)]
## clustering

ks <- 1:50
tot_within_ss <- sapply(ks, function(k) {
  cl <- kmeans(nips_Data[c(1:nrow(nips_Data)),c(2:10)], k, nstart = 10)
  cl$tot.withinss
})
plot(ks, tot_within_ss, type = "b")

data(iris)
i <- grep("Length", names(iris))
x <- iris[, i]
cl <- kmeans(x, 3, nstart = 10)
plot(x, col = cl$cluster)


set.seed(12)
init <- sample(3, nrow(x), replace = TRUE)
plot(x, col = init)



par(mfrow = c(1, 2))
plot(x, col = init)
centres <- sapply(1:3, function(i) colMeans(x[init == i, ], ))
centres <- t(centres)
points(centres[, 1], centres[, 2], pch = 19, col = 1:3)

tmp <- dist(rbind(centres, x))
tmp <- as.matrix(tmp)[, 1:3]

ki <- apply(tmp, 1, which.min)
ki <- ki[-(1:3)]

plot(x, col = ki)
points(centres[, 1], centres[, 2], pch = 19, col = 1:3)


par(mfrow = c(1, 1))

ks <- 1:10
tot_within_ss <- sapply(ks, function(k) {
  cl <- kmeans(x, k, nstart = 10)
  cl$tot.withinss
})
plot(ks, tot_within_ss, type = "b")

library(tidyverse)  # data manipulation
library(cluster)    # clustering algorithms
library(factoextra) # clustering algorithms & visualization

# function to compute average silhouette for k clusters
avg_sil <- function(k) {
  km.res <- kmeans(x, centers = k, nstart = 25)
  ss <- silhouette(km.res$cluster, dist(x))
  mean(ss[, 3])
}

# Compute and plot wss for k = 2 to k = 15
k.values <- 2:20

# extract avg silhouette for 2-15 clusters
avg_sil_values <- map_dbl(k.values, avg_sil)

plot(k.values, avg_sil_values,
     type = "b", pch = 19, frame = FALSE, 
     xlab = "Number of clusters K",
     ylab = "Average Silhouettes")



fviz_nbclust(x, kmeans, method = "silhouette")


set.seed(123)
final <- kmeans(x, 2, nstart = 25)

fviz_cluster(final, data = x)
