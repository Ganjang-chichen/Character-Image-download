#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
import time
import json
import urllib.request
import os
import sys
from PIL import Image

import json
from collections import OrderedDict

def find_user (name) :
    user_url = "https://maplestory.nexon.com/Ranking/World/Total?c=" + name
    
    res = requests.get(user_url)
    user_info = BeautifulSoup(res.content, 'html.parser')
    
    if user_info.find('div', {'class' : 'none_list2'}) :
        print("닉네임: no data")
        print("길드명: no data")
        return "no data"
    else :
        table = user_info.find('tbody')

        if table :
            for tr in table.find_all('tr'):      # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
                tds = list(tr.find_all('td'))    # 모든 <td> 태그를 찾아서 리스트로 만듦

                a = tr.find('a')
                parse_name = tds[1].find('a').text
                guild_name = tds[5].text
                img_src = tds[1].find('img')['src']
                if(parse_name == name) :
                    print("닉네임: " + parse_name)
                    print("길드명: " + guild_name)
                    
                    return img_src
                


# In[6]:


def downloadIMG (name) :
    url = find_user(name)
    if(url == "no data") :
        print("일치하는 케릭터가 존재하지 않습니다.")
        return
    else :
        urllib.request.urlretrieve(url, name + ".png")
        print("다운로드 완료!")
        img = Image.open(name + ".png")
        img.show()


# In[4]:


def init() :
    print("이 프로그램은 메이플 스토리 케릭터 이미지파일 다운로더 입니다.\n")
    print("케릭터의 닉네임을 입력해주세요.\n")
    print("닉네임 : ")
    nickname = input()
    downloadIMG(nickname)
    


# In[7]:


init()

