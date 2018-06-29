# 서울시 골목상권 15개 업종에 대한 상관관계 분석하기

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

# NA 값이 있는 행 제거하기
data15 <- na.omit(data15)

# 커피음료만 분석 (이상치 확인해보니 top3개만 비정상적으로 큰 매출. 효과적 분석을 위해 3행 제거)
data15_coffee <- data15[c(order(-data15$커피음료)),]
head(data15_coffee)
data15_coffee <- data15_coffee[-c(1,2,3),]
cor_data_result <- cor(data15_coffee)
cor_data_result

# 15개 업종 상관관계 분석 결과 저장하기
setwd("C:/seoul_bigdata")
write.csv(cor_data_result, file="cor_data_result.csv", row.names=TRUE)

# 커피음료 매출과 상관관계가 높은 순으로 나열하여 데이터 확인
coffee <- cor_data_result[,'커피음료']
coffee <- sort(coffee, decreasing = T)
coffee

# 한식음식점 매출을 분석하기 위해 원본 데이터 다시 로딩(커피음료 분석을 위해 3개 이상치를 제거 했었음) 
# 한식음식점 매출과 상관관계가 높은 순으로 나열하여 데이터 확인 
data15_korean <- data15[c(order(-data15$한식음식점)),]
head(data15_korean)
cor_data_result <- cor(data15_koren)
korean <- cor_data_result[,'한식음식점']
korean <- sort(korean, decreasing = T)
korean

# 산점도 및 1:1 상관관계 확인 
plot(호프간이주점~커피음료, data=data15_coffee)
fit <- lm(호프간이주점~커피음료, data=coffee)
summary(fit)




