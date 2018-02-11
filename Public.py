import base64
import hashlib
import hmac
import json
import time
from urllib.request import urlopen, Request
import requests
HOST = 'https://api.coinone.co.kr/'
'''
권한이 public인 api의 경우 모습을 살짝 수정하여 post가 아닌 get방식으로
데이터를 가져오는 식으로 수정하였습니다.
parameter에 따라 다른 데이터를 가져올 수 있도록 get메소드에 인자를 넣는식으로 수정
'''
def get_response(url,param):
    params = {
        'currency' : param
    }
    api_url = HOST + url
    req = requests.get(api_url, params=params)
    return json.loads(req.text)

def orderbook(param):
    data = get_response('/orderbook', param)
    return data

def ticker(param):
    data = get_response('/ticker', param)
    return data

def recentCompleteOrders(param):
    data = get_response('/trades', param)
    return data
