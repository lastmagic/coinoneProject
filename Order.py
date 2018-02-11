import base64
import hashlib
import hmac
import json
import time
import Manage_Token_Key
from urllib.request import urlopen, Request
'''
Order에 해당하는 api를 한 파일에 모아서 관리하고있습니다.

ACCESS_TOKEN과 SECRET_KEY의 경우 사용자로부터 입력을 받아 파일로 입출력을 진행하고있습니다.
'''
ACCESS_TOKEN,SECRET_KEY = Manage_Token_Key.read_token_key()
UPPERCASE_SECRET_KEY = SECRET_KEY.upper()
HOST = 'https://api.coinone.co.kr/'


def get_base_payload():
    return {
        'access_token': ACCESS_TOKEN,
    }


def str_2_byte(s, encode='utf-8'):
    return bytes(s, encode)


def get_encoded_payload(payload):
    payload['nonce'] = int(time.time() * 1000)
    dumped_json = json.dumps(payload)
    encoded_json = base64.b64encode(str_2_byte(dumped_json))
    return encoded_json


def get_signature(encoded_payload):
    signature = hmac.new(str_2_byte(UPPERCASE_SECRET_KEY), encoded_payload, hashlib.sha512)
    return signature.hexdigest()


def get_response(url, payload):
    encoded_payload = get_encoded_payload(payload)
    signature = get_signature(encoded_payload)
    headers = {
        'Content-Type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': signature,
    }
    api_url = HOST + url
    req = Request(api_url, data=encoded_payload, headers=headers, method='POST')

    with urlopen(req) as res:
        data = res.read().decode('utf-8')
        return json.loads(data)


def create_payload(data):
    payload = get_base_payload()
    payload.update(data)
    return payload

def cancelOrder():
    data = get_response('v2/order/cancel/', create_payload({
        'order_id': "{order_id}",
        'price': 50000000,
        'qty': 0.1,
        'currency': 'btc',
        'is_ask': 0,
    }))
    return data

def limitBuy():
    payload = get_base_payload()
    payload.update({
        'price': 50000,
        'qty': 0.1,
        'currency': 'btc'
    })
    data = get_response('v2/order/limit_buy/', payload)
    return data

def limitSell():
    data = get_response('v2/order/limit_sell/', create_payload({
        'price': 50000000,
        'qty': 0.1,
        'currency': 'btc',
    }))
    return data

def myCompleteOrders():
    data = get_response('v2/order/complete_orders/', create_payload({
        'currency': 'btc',
    }))
    return data

def myLimitOrders():
    data = get_response('v2/order/limit_orders/', create_payload({
        'currency': 'btc',
    }))
    return data

def myOrderInformation():
    data = get_response('v2/order/order_info/', create_payload({
        'order_id': 'a06de5d0-b2cd-4064-be88-334f06b0b0c9',
        'currency': 'btc',
    }))
    return data
