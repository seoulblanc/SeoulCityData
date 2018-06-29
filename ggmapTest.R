# 좌표(위도, 경도) 데이터를 가지고 ggmap, ggplot2 패키지를 이용하여 지도에 상권 위치 표시
# 코드 참고: http://dbrang.tistory.com/1054 [dBRang [dɪ'·bɪ·raŋ]]

library(ggplot2)
library(ggmap)

# 데이터 로딩 
street = read.csv("C:/Rwork/street_GJ2.csv",header=T)
street

gc = geocode("Gwangjingu, seoul, korea", source="google")
gc

# -- 레이어1 : 정적 지도 생성
kor = get_map(gc, zoom=14, maptype = "roadmap")
# maptype : roadmap, satellite, terrain, hybrid, watercolor

# -- 레이어2 : 지도위에 포인트
ggmap(kor) + geom_point(data=street, aes(x=LON, y=LAT, color=factor(상권명)), size=8)
kor.map = ggmap(kor) + geom_point(data=street, aes(x=LON, y=LAT, color=factor(상권명)), size=7)

# -- 레이어3 : 지도위에 텍스트 추가
kor.map + geom_text(data=street, aes(x=LON+0.01, y=LAT+0.01, label=상권명), size=3)
# LAT+0.01 : 텍스트 위치(포인트의 0.01 위쪽)
# geom_text : 텍스트 추가

# -- 지도 저장
#    넓이, 폭 적용 파일 저장
ggsave("C:/Rwork/street1.png",width=10.24,height=7.68)

# -- 밀도 적용 파일 저장
ggsave("C:/Rwork/street2.png",dpi=1000) 
# 9.21 x 7.68 in image



