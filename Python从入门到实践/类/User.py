# coding=utf-8
class user():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.attempts = 0

    def describe_user(self):
        print('第一个名字：%s,第二个名字：%s,' %(self.first_name,self.last_name))
    def greet_user(self):
        print('hello!,%s%s' %(self.first_name,self.last_name))
    def increment_login_attempts(self):
        self.attempts += 1
        print(self.attempts)
    def reset_login_attempts(self):
        self.attempts = 0
        print(self.attempts)

user = user('aaa','bbb')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()