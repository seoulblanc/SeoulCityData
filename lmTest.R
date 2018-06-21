
setwd("C:/seoul_bigdata")
data03 <- read.table("test0619_02.txt", header=T, 
                     na.strings = "NA", fileEncoding="UTF-16LE", sep = "\t")
head(data03)

colnames(data03) <- c("street", "coffee", "conv", "koreanfood", "sum", "popul")
plot(conv~popul, dat=data03)
fit <- lm(conv~popul, dat=data03)
summary(fit)

colnames(data03) <- c("street", "coffee", "conv", "koreanfood", "sum", "popul")
plot(koreanfood~popul, dat=data03)
fit <- lm(koreanfood~popul, dat=data03)
summary(fit)
