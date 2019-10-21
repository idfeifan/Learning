# coding=utf-8
import json
#json.dump()接收两个参数，要存储的数据以及可用于存储数据的文件对象
def number_writer():
    numbers = [2,3,5,7,11,13]
    file_name = 'number.json'
    with open(file_name,'w') as f_obj:
        json.dump(numbers,f_obj)

def remember_me():
    username = input('what is you name?')
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)

        print("we'll remember you when you come back," + username + '!')
def greet_user():
    filename = 'username.json'
    with open(filename,'r') as f_obj:
        username = json.load(f_obj)

    print("welcom back, " + username + "!")
def remember_me2():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is you name ?")
        with open(filename) as f_obj:
            json.dump(username,f_obj)
            print("we'll remember you when you come back," + username + '!')
    else:
        print("welocome back," + username + "!")
greet_user()