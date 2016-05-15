#-*- coding: utf-8 -*-
def T(N, Beg, Aux, End):
	if N == 1:
		print(Beg, '->', End)
	else:
		T(N-1, Beg, End, Aux)
		T(1, Beg, Aux, End)
		T(N-1, Aux, Beg, End)
#N=원판의수, BEG,AUX,END 기둥
#재귀 알고리즘을 활용
T(3,'A','B','C')
T(5,'A','B','C')
		
