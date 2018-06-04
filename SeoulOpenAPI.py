import json
import requests

URL1 = 'http://openapi.seoul.go.kr:8088/'
KEY = ''
URL2 = '/json/InfoTrdarSelng/1/20/201702'  # 파일타입/원하는데이터이름/페이지시작/페이지끝/년월
URL = URL1 + KEY + URL2
print(URL)
print("URL 요청 성공!")

def request_url():
    try:
        source_code = requests.get(URL)
        plain_text = source_code.text
        mydatas = json.loads(plain_text)
        return mydatas
    except Exception as e:
        print(e)
        print("Error for URL")

def getData():
    list01 = []
    mydatas = request_url()
    for comment in mydatas['InfoTrdarSelng']['row']:
        list01.append(comment['TRDAR_CD_NM'])
        list01.append(comment['THSMON_SELNG_AMT'])
        list01.append('남/여 매출 비율:')
        list01.append(comment['ML_SELNG_RATE'])
        list01.append(comment['FML_SELNG_RATE'])
        list01.append('20대 매출 비율:')
        list01.append(comment['AGRDE_20_SELNG_RATE'])
    print(list01)

if __name__ == "__main__":
    getData()

