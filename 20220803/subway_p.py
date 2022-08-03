#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def connect(date):
    key='41475a746d68696f3938776c425278'          #부여받은 인증키 지정
    date=str(date)                                   #date는 i 라는 int형에서 문자열로 변환하여 지정
    url1='http://openapi.seoul.go.kr:8088/'+key   #url1에 키 값까지
    url2='/xml/CardSubwayStatsNew/1/1000/'+date   #url2에 date 값까지
    url=url1+url2                                 #url1과 url2가 합쳐진 url 생성
    xml=requests.get(url)                         #xml 변수에 request.get(url) 을 지정
    if xml.status_code!=200:
        print('연결실패, 서버로부터 데이터를 가져오지 못했습니다.')
        return
    return xml


def subway_p(date):
    xml=connect(date)
    if xml==None:
        return
    
    soup=bs(xml.text,'html.parser')               #soup 변수에 bs함수로 xml을 html 해석기를 사용헤 text만 불러옴

    items=soup.find_all('row')                    #items 변수에 r각 row안의 값들을 지정

    ls=['use_dt','line_num','sub_sta_nm','ride_pasgr_num','alight_pasgr_num','work_dt'] #ls에 가져올 row열 이름들 지정

    res=[]                                        #res 빈 리스트 생성
    for item in items:                           #items 중에 item만큼 실행
        dt={}                                      #dt 빈 딕셔너리 생성
        for j in ls:                               # ls 중에 j만큼 실행
            try:                                     #우선 실행
                dt[j]=item.find(j).text              #j에 해당하는 열의 행값들을 text만 가져옴
            except:                                 #실행 실패시
                dt[j]=None                          #dt[j] 리스트에 'None'값 반환
        res.append(dt)                            #dt 딕셔너리가 완성되면 res 리스트에 전송

    df=pd.DataFrame(res)
    return df

if __name__=='__main__':
    print('--종료--')
    df=subway_p('20220730')
    display(df)

#     df=pd.DataFrame(res)                          #판다스 데이터프레임 기능으로 res 리스트를 df로 지정 
#     df.to_csv(f'./지하철/{date}.csv')             #df를 미리 생성해놓은 지하철 폴더에 csv 로 저장 (20220701.csv~)
# print('end')                                      #for문 종료시 'end'를 화면에 출력


# In[ ]:





# In[ ]:




