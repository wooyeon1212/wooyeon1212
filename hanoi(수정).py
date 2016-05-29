#-*- coding: utf-8 -*-
count=0
#count를 변수로 지정해서 시행 횟수를 나타내고자 하였으나 따로 구할수가 없네요...어떻게 짜야할지를 모르겠습니다.
def T(N, Beg, Aux, End):
        count+=1
	if N == 1:
                
		print(Beg, '->', End)
	else:
		T(N-1, Beg, End, Aux)
		T(1, Beg, Aux, End)
		T(N-1, Aux, Beg, End)
#N=원판의수, BEG,AUX,END 기둥
#재귀 알고리즘을 활용
while (1):
        n=input()
        #n을 원판의 개수로 하여 구 input을 받도록 하였습니다.
        T(n,'A','B','C')

		
