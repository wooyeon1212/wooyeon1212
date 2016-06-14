#-*- coding: utf-8 -*-
#1 부터 1000사이의 숫자를 입력하면 컴퓨터가 찾아 나가는 프로그램 while문을 사용해서 구현했습니다.

while (1):
    
    print "I'will guess your number between 1 and 1000"
    number=raw_input('enter your number: ')
    print 'guess start'
    number=int(number)
    high=1000
    low=1
    import time
    import random
    guess= random.randint(1,1000)
    while number!=guess:
        if number<guess:
            time.sleep(1)
            print 'my guess is ' +str(guess)
            time.sleep(1)
            print ' too big'
            high=guess
            guess=(high+low)/2
        else :
            time.sleep(1)
            print 'my guess is ' +str(guess)
            time.sleep(1)
            print 'too low'
            low=guess
            guess=(high+low)/2
    print ' my answer is' + str(guess)            
