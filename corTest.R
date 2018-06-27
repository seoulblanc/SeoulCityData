
setwd("C:/seoul_bigdata/201803시간대별csv")
data <- read.table("201803_allday_coffee.csv", header=T, 
                   na.strings = "NA", fileEncoding="UTF-16LE", sep = ",")
head(data)
dim(data)

data_set <- data[,-c(1,44)]
data15 <- subset(data, select=c(
한식음식점,
슈퍼마켓,
일반의원,
편의점,
의류점,
일식집,
양식집,
약국,
호프간이주점,
커피음료,
치과의원,
분식집,
중국집,
입시보습학원,
예체능학원))
dim(data15)

head(data15)
data15 <- na.omit(data15)

#커피피음료만 분석 (이상치 확인후 top3개 제거)
data15_coffee <- data15[c(order(-data15$커피음료)),]
head(data15_coffee)
data15_coffee <- data15_coffee[-c(1,2,3),]
cor_data_result <- cor(data15_coffee)

cor_data_result
setwd("C:/seoul_bigdata")
write.csv(cor_data_result, file="cor_data_result.csv", row.names=TRUE)


coffee <- cor_data_result[,'커피음료']
coffee <- sort(coffee, decreasing = T)
coffee

#한식음식점 분석
data15_korean <- data15[c(order(-data15$한식음식점)),]
head(data15_korean)
cor_data_result <- cor(data15_koren)
korean <- cor_data_result[,'한식음식점']
korean <- sort(korean, decreasing = T)
korean

plot(호프간이주점~커피음료, data=data15_coffee)
fit <- lm(호프간이주점~커피음료, data=coffee)
summary(fit)




