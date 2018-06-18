import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

URL1 = 'http://openapi.seoul.go.kr:8088/'
KEY = ''
URL2 = '/json/InfoTrdarSelng/1000/1999/201803'  # 파일타입/원하는데이터이름/시작_인덱스/끝_인덱스/년월
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

def get_data():
    result = []
    mydatas = request_url()
    print(mydatas)
    for comment in mydatas['InfoTrdarSelng']['row']:
        result_sub = []
        result_sub.append(comment['STDR_YM_CD']) #기준_년월_코드
        result_sub.append(comment['TRDAR_CD_NM']) #상권_코드_명
        result_sub.append(comment['SVC_INDUTY_CD_NM']) #서비스_업종_코드_명
        result_sub.append(comment['THSMON_SELNG_AMT']) #당월매출
        result_sub.append(comment['ML_SELNG_AMT'])  # 남성매출액
        result_sub.append(comment['FML_SELNG_AMT'])  # 여성매출액
        result_sub.append(comment['STOR_CO']) #점포수
        result.append(result_sub)
    # print(result)
    print('크롤링 및 데이터 가져오기 성공')
    return result

def dataframe_sorting():
    result = get_data()
    data = pd.DataFrame(result, columns=("일자", "상권_코드_명", "서비스_업종_코드_명", "당월매출","남성매출액","여성매출액", "점포수"))
    print('데이터 프레임 만들기 성공')
    print(data)
    print('데이터의 길이는?')
    print(len(data))
    return data

def data_plt():
    data = dataframe_sorting()
    a = data.loc[data["서비스_업종_코드_명"] == "일식집"]
    x = a["남성매출액"]
    y = a["당월매출"]
    plt.scatter(x, y)
    plt.show()

if __name__ == "__main__":
    data_plt()




