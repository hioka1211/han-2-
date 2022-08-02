#!/usr/bin/env python
# coding: utf-8

# In[1]:


# def client_gmap():
#     import googlemaps
#     gmaps_key = "AIzaSyCZvnX7q7qlQxNNy3wnLKHxlz2xo6sStSI" # 자신의 key를 사용합니다.
#     gmaps = googlemaps.Client(key=gmaps_key) #구글maps Api 웹 서비스를 요청합니다.


def get_addr(text):
    import googlemaps
    gmaps_key = "AIzaSyCZvnX7q7qlQxNNy3wnLKHxlz2xo6sStSI" # 자신의 key를 사용합니다.
    gmaps = googlemaps.Client(key=gmaps_key) #구글maps Api 웹 서비스를 요청합니다.
    tmp=gmaps.geocode(text, language='ko') #경복궁 지도 정보를 가져옵니다.
    addr=tmp[0]['formatted_address']
    return addr

def get_lat(text):
    import googlemaps
    gmaps_key = "AIzaSyCZvnX7q7qlQxNNy3wnLKHxlz2xo6sStSI" # 자신의 key를 사용합니다.
    gmaps = googlemaps.Client(key=gmaps_key) #구글maps Api 웹 서비스를 요청합니다.
    tmp=gmaps.geocode(text, language='ko') #경복궁 지도 정보를 가져옵니다.
    lat=tmp[0]['geometry']['location']['lat']
    return lat

def get_lng(text):
    import googlemaps
    gmaps_key = "AIzaSyCZvnX7q7qlQxNNy3wnLKHxlz2xo6sStSI" # 자신의 key를 사용합니다.
    gmaps = googlemaps.Client(key=gmaps_key) #구글maps Api 웹 서비스를 요청합니다.
    tmp=gmaps.geocode(text, language='ko') #경복궁 지도 정보를 가져옵니다.
    lng=tmp[0]['geometry']['location']['lng']
    return lng


# In[ ]:




