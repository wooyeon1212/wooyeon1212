#-*- coding: utf-8 -*-
#컴퓨터가 랜덤한 숫자를 생성하면 그것을 추측해보는 프로그램
print 'hello! what is your name?'
name= raw_input()
print ' well, ' + name + '  i and thinking of a number between 1 and 20 '
print 'take a guess'
import random
x=random.randint(1,20)
chance=0
    while chance<6 :
        g=raw_input()
        g=int(g)
        chance= chance +1
        if x<g :
            print 'it is too high'
        if x>g :
            print 'it is too low'
        if x==g :
            print 'good'
        



