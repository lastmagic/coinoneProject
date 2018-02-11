def read_token_key():
    with open('user.txt', 'r') as file:
    	ACCESS_TOKEN = file.readline()
    	SECRET_KEY = file.readline()
    	ACCESS_TOKEN=ACCESS_TOKEN.strip('\n')
    	SECRET_KEY=SECRET_KEY.strip('\n')
    return ACCESS_TOKEN,SECRET_KEY

def enter_token_key():
    print("Enter your Token & Key")
    with open('user.txt', 'w') as file:
        ACCESS_TOKEN = input("ACCESS_TOKEN:") +'\n'
        SECRET_KEY = input("SECRET_KEY:") +'\n'
        file.write(ACCESS_TOKEN)
        file.write(SECRET_KEY)
