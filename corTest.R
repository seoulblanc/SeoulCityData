
setwd("C:/seoul_bigdata/201711시간대별csv")
data <- read.table("allday.csv", header=T, 
                     na.strings = "NA", fileEncoding="UTF-16LE", sep = ",")
data10 <- subset(data, select=c(편의점, 미용실, 호프간이주점, 
        제과점, 패스트푸드점, 분식집, 양식집, 일식집, 한식음식점,커피음료))

data10 <- na.omit(data10)
data10 <- data10[c(order(-data10$커피음료)),]
data10 <- data10[-c(1),]
#data10 <- data10[-c(1,2,3),]

head(data10)
dim(data10)

cor_data_result <- cor(data10)
coffee <- cor_data_result[,'커피음료']
coffee <- sort(coffee, decreasing = T)
coffee

write.csv(data10, file="201711_9category.csv", row.names=TRUE)
