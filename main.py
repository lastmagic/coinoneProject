import Manage_Token_Key #Token,Key를 관리하는 파일
import Account #Account에 해당되는 메소드들을 관리하는 파일
import Order #Order에 해당되는 메소드들을 관리하는 파일
import Transaction #Transaction에 해당되는 메소드들을 관리하는 파일
import Public #Public에 해당되는 메소드들을 관리하는 파일
import os #cls()함수를 정의하여 사용하기위해 추가
from urllib.request import urlopen, Request
HOST = 'https://api.coinone.co.kr/'

'''
출력되는 문자열을 모두 변수로 관리합니다.
'''
menu = 'Select category\n1. Private 2. Public 3. Enter Key&Token 4. Exit'

private = 'Choose the category\n1. Account 2. Order 3. transaction'

account = 'Choose the function\n1. Balance 2. dailyBalance 3. depositAddress 4. userInformation 5. virtualAccount'

order = 'Choose the function\n1. cancelOrder 2. limitBuy 3. limitSell 4. myCompleteOrders 5. myLimitOrders 6. myOrderInformation'

transaction = 'Choose the function\n1. twoFactorAuthentication 2. coinTransactionsHistory 3. krwTransactionHistory'

public = 'Choose the function\n1. orderbook 2. ticker 3. recentCompleteOrders'

parameter = 'Enter the kind of Coin ex)btc, bch, eth, etc, xrp, qtum, iota, ltc, btg'

error = 'Name Description\n\
4 Blocked user access\n\
11 Access token is missing\n\
12 Invalid access token\n\
40 Invalid API permission\n\
50 Authenticate error\n\
51 Invalid API\n\
52 Deprecated API\n\
53 Two Factor Auth Fail\n\
100 Session expired\n\
101 Invalid format\n\
102 ID is not exist\n\
103 Lack of Balance\n\
104 Order id is not exist\n\
105 Price is not correct\n\
106 Locking error\n\
107 Parameter error\n\
111 Order id is not exist\n\
112 Cancel failed\n\
113 Quantity is too low(ETH, ETC > 0.01)\n\
120 V2 API payload is missing\n\
121 V2 API signature is missing\n\
122 V2 API nonce is missing\n\
123 V2 API signature is not correct\n\
130 V2 API Nonce value must be a positive integer\n\
131 V2 API Nonce is must be bigger then last nonce\n\
132 V2 API body is corrupted\n\
141 Too many limit orders\n\
150 It is V1 API. V2 Access token is not acceptable\n\
151 It is V2 API. V1 Access token is not acceptable\n\
200 Wallet Error\n\
202 Limitation error\n\
210 Limitation error\n\
220 Limitation error\n\
221 Limitation error\n\
310 Mobile auth error\n\
311 Need mobile auth\n\
312 Name is not correct\n\
330 Phone number error\n\
404 Page not found error\n\
405 Server error\n\
444 Locking error\n\
500 Email error\n\
501 Email error\n\
777 Mobile auth error\n\
778 Phone number error\n\
1202 App not found\n\
1203 Already registered\n\
1204 Invalid access\n\
1205 API Key error\n\
1206 User not found\n\
1207 User not found\n\
1208 User not found\n\
1209 User not found'
#화면 출력지움
def printError(ret):
    print('Error Occur errorCode:'+ret['errorCode'])
    print(error)
def cls():
    os.system('clear')
#메뉴출력
def printMenu():
    cls()
    print(menu)
#Account에 번호에 해당되는 함수를 실행하여 에러가 발생하지 않았을경우 결과출력 에러발생시 에러코드 출력
def printAccount(num):
    if num ==1:
        ret = Account.balance()
    elif num==2:
        ret = Account.dailyBalance()
    elif num==3:
        ret = Account.depositAddress()
    elif num==4:
        ret = Account.userInformation()
    elif num==5:
        ret = Account.virtualAccount()
    if ret['errorCode'] == '0':
        print(ret)
    else:
        printError(ret)
#Order에 번호에 해당되는 함수를 실행하여 에러가 발생하지 않았을경우 결과출력 에러발생시 에러코드 출력
def printOrder(num):
    if num ==1:
        ret = Order.cancelOrder()
    elif num==2:
        ret = Order.limitBuy()
    elif num==3:
        ret = Order.limitSell()
    elif num==4:
        ret = Order.myCompleteOrders()
    elif num==5:
        ret = Order.myLimitOrders()
    elif num==6:
        ret = Order.myOrderInformation()
    if ret['errorCode'] == '0':
        print(ret)
    else:
        printError(ret)
#Transaction에 번호에 해당되는 함수를 실행하여 에러가 발생하지 않았을경우 결과출력 에러발생시 에러코드 출력
def printTransaction(num):
    if num==1:
        ret = Transaction.twoFactorAuthentication()
    elif num==2:
        ret = Transaction.coinTransactionsHistory()
    elif num==3:
        ret = Transaction.krwTransactionHistory()
    if ret['errorCode'] == '0':
        print(ret)
    else:
        printError(ret)
#Public에 번호에 해당되는 함수를 실행하여 에러가 발생하지 않았을경우 결과출력 에러발생시 에러코드 출력
def printPublic(num, param):
    if num==1:
        ret = Public.orderbook(param)
    elif num==2:
        ret = Public.ticker(param)
    elif num==3:
        ret = Public.recentCompleteOrders(param)
    if ret['errorCode'] == '0':
        print(ret)
    else:
        printError(ret)

if __name__ == '__main__':
    print("Start Promgram")
    while True :
        printMenu()
        sel = int(input())
        if sel == 4:
            break
        elif sel == 3:
            Manage_Token_Key.enter_token_key()
        elif sel == 2:
            num = int(input(public+'\n'))
            param = input(parameter+'\n')
            printPublic(num, param)
        elif sel == 1:
            num = int(input(private+'\n'))
            if num == 1:
                n = int(input(account+'\n'))
                printAccount(n)
            elif num == 2:
                n = int(input(order+'\n'))
                printOrder(n)
            elif num == 3:
                n = int(input(transaction+'\n'))
                printTransaction(n)
        else:
            pass
        restart = int(input("Do you want to start again?\n1.YES 2.NO\n"))
        if restart == 2:
            break
