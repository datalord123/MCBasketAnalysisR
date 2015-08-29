library(arules)
library(arulesViz)
library(datasets)
library(t)

#Load the DataSet
Groceries<- read.transactions('groceries.csv',format = 'basket',sep=',',rm.duplicates = TRUE)


read