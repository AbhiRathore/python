tabl=read.csv("D:/kaggle_redhat/Statistics/case1/date_sample.csv",header=T,na.strings=c("",NA))
head(tabl)
names(tabl)
str(tabl)
tabl$Contents=as.character(tabl$Contents)# converting content in character

#### function to extract date , u may rename it :P
date_ASR=function(x){
  library(stringr)
  c=str_extract_all(x,'\\d+\\/\\w+\\/\\d+')
  if(c == 'character(0)'){ 
    c1=str_extract_all(x,'\\d+\\-\\w+\\-\\d+')
  if(c1== 'character(0)'){
    c2=str_extract_all(x,'\\w+\\s\\d+(st)?(nd)?(rd)?(th)?,\\s+\\d+')
  if(c2== 'character(0)'){
    c3=str_extract_all(x,'\\d+\\W+\\w+\\W+\\d+')
    if(c3=='character(0)'){c4=str_extract_all(x,'\\d+\\w+\\d+')
    if(c4=='character(0)'){return("nul")}
    
    else return(c4[[1]])
    
    }
    
    else return(c3[[1]])
    
      }
    
    else return(c2[[1]])
  }
    else return(c1[[1]])
    } 
  else return(c[[1]])
}

try="the convenience of using appbased cabs has caught on  July 11 in 2015 on so much in the last 
couple of years that almost everyone with a smartphone is likely to have an uber or ola app installed 
on their phone there is no denying"
try2="convenience of using appbased cabs has caught on 12 Jul 2015 on so much in the
         last couple of years at 2 parker 456 place z"
str_extract_all(try,'\\d+\\w+\\d+')
str_extract_all(try,'\\d+\\W+\\w+\\W+\\d+')
length(v)
date_ASR(try)
nrow(tabl)
### trial on our file , creating a new column by the name date_ext
for(i in 1:nrow(tabl)){
tabl$date_ext[i]=date_ASR(tabl$Contents[i])
}
library(dplyr)
ncol(tabl)
###  check it 
head(tabl[,15],16)

## for all date value it will give extracted dates and if date is not there it will give nul  
############### ENJOY  HAIL BM!!!!!! 

