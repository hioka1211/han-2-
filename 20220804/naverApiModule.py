#!/usr/bin/env python
# coding: utf-8

# In[20]:


# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
import pandas as pd

def connect(검색어, api='blog'):
    client_id = "0p4Rd8xJQxVRre_lMgBa"
    client_secret = "SBObTGPumD"
    encText = urllib.parse.quote(검색어)
    url = 'https://openapi.naver.com/v1/search/'+api+'?query=' + encText +'&display=100&start=1'# json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode!=200):
        print("Error Code:" + rescode)
        return           
    response_body = response.read()
    response=json.loads(response_body)
    return response

def naver_api(검색어,api='blog'):
    '''
    naver_api(검색어,api='blog')
    api='blog'(default) 'news | cafearticle | kin | book | encyc | movie'
     
     'news(뉴스) | cafearticle(카페글) | kin(지식인) | book(책검색) | encyc(백과사전) | movie(영화검색)'

    '''
    response=connect(검색어, api)
    df=pd.DataFrame(response['items'])
    return df

def total_count(검색어,api='blog'):
    '''
    total_count(검색어,api='blog')
    api='blog'(default) 'news | cafearticle | kin | book | encyc | movie'
     
     'news(뉴스) | cafearticle(카페글) | kin(지식인) | book(책검색) | encyc(백과사전) | movie(영화검색)'

    '''
    response=connect(검색어, api)
    total=response['total']
    return total

if __name__=='__main__':
    t=total_count('파이썬','book')
    print(t)
#     df=naver_api('파이썬')
#     display(df)


# In[ ]:




