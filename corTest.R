
setwd("C:/seoul_bigdata/201803시간대별csv")
data <- read.table("21_24.csv", header=T, 
                     na.strings = "NA", fileEncoding="UTF-16LE", sep = ",")

data6 <- data[ , 32:40]
data6 <- na.omit(data6)

table1 <- cor(data1)
table2 <- cor(data2)
table3 <- cor(data3)
table4 <- cor(data4)
table5 <- cor(data5)
table6 <- cor(data6)

table_all <- rbind(table1, table2, table3, table4, table5, table6)
table_all

write.csv(table_all, file="time_table_all.csv", row.names=TRUE)

#data11 <- subset(data, select=c(중국집,화장품))
#data11 <- na.omit(data11)
#data11

#plot(중국집~커피음료, dat=data11)
#fit <- lm(중국집~커피음료, dat=data11)
#summary(fit)
