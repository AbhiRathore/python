library(ggplot2)
library(gridExtra)
library(data.table)
library(dplyr)

emp1=read.csv("NO.csv",header = T,na.strings = c("na",NA,"")) # to read the file
emp1$Calculated.Target.Date=as.character(emp1$Calculated.Target.Date) # to change type(property) of a column
emp1=as.data.table(emp1) # converting to data table
emp3=emp1[,.(Calculated.Status,IdentityType,Calculated.Target.Date)] # selecting out three columns
emp4=group_by(emp3,Calculated.Target.Date) # Grouping on basis of date
# selecting employee and contractor data sets distinctly
emp_e=filter(emp4,IdentityType=="Employee") 
emp_c=filter(emp4,IdentityType=="Contractor")
emp5=summarise(emp_e,identity_type=unique(Calculated.Status),count=n()) # summarising based on calculated status
emp6=summarise(emp_c,identity_type=unique(Calculated.Status),count=n()) # summarising based on calculated status
p=ggplot(emp5, aes(Calculated.Target.Date ,identity_type,label=count,fill=count)) +geom_point()+geom_label(color="white",aes(label=count),hjust=0, vjust=1)+
geom_density(position = "stack")+ggtitle("Employee") +xlab("Date") + ylab("Identity type")+theme(
  plot.title = element_text(color="red", size=14, face="bold.italic"),
  axis.title.x = element_text(color="blue", size=14, face="bold"),
  axis.title.y = element_text(color="#993333", size=14, face="bold")
)

q=ggplot(emp6, aes(Calculated.Target.Date ,identity_type,label=count,fill=count)) +geom_point()+geom_label(color="white",aes(label=count),hjust=0, vjust=1)+
  geom_density(position = "stack")+ggtitle("Contractor") +xlab("Date") + ylab("Identity type")+theme(
    plot.title = element_text(color="red", size=14, face="bold.italic"),
    axis.title.x = element_text(color="blue", size=14, face="bold"),
    axis.title.y = element_text(color="#993333", size=14, face="bold")
  )

grid.arrange(p,q,ncol=1) # to add both plots together
