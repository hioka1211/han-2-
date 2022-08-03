#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_code(name):
    try:
        df_code=pd.read_csv('./기상청_지역코드.csv', encoding='cp949')
        code=int(df_code[df_code['지점명']==name]['지점'])
    except FileNotFoundError:
        print('파일이 없습니다.')
        return
    except Exception as e:
        print('해당지역이 없습니다.', e)
        return
    return code


# In[ ]:




