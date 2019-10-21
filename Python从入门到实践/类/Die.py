# coding=utf-8
from random import randint
"""投掷骰子"""
class Die():
    def __init__(self,sides=6):
        self.sides = sides


    def roll_die(self):
        i = 0
        while i < 10:

            x = randint(1,self.sides)
            print(x)
            i+=1

die = Die(10)
die.roll_die()