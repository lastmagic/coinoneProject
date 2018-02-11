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
#화면 출력지움
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
        print('Error Occur errorCode:'+ret['errorCode'])
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
        print('Error Occur errorCode:'+ret['errorCode'])
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
        print('Error Occur errorCode:'+ret['errorCode'])
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
        print('Error Occur errorCode:'+ret['errorCode'])

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
