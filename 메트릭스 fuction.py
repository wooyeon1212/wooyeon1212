#-*- coding: utf-8 -*-
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[1,2,3],
    [4,5,6],
    [7,8,9]]

#add matrix
def add(X,Y):
#result 함수를 임의로 만든 다음 result 값을 대입하도록 설계했습니다.
    result=[[row for row in range(len(X))] for col in range(len(X[0]))]
    #각 메트릭스 요소들이 더해지도록 for in range를 사용하였습니다.
    for row in range(len(X)):
       for col in range(len(X[0])):
           result[row][col] = X[row][col] + Y[row][col]
    return result


#multiply matrix
def multiply(X,Y):
    #result 함수를 임의로 만든 다음 result 값을 대입하도록 설계했습니다.
    result=[[0 for row in range(len(X))] for col in range(len(X[0]))]
    #각 메트릭스 요소들을 곱하기위해 for in range를 사용하였습니다.
    #행렬X 의 row를 i로 지정,Y의 col을 j로,Y의 row를 로 지정하여 곱셈 연산을 수행하도록 만들었습니다.
    for i in range(len(X)):
       for j in range(len(Y[0])):
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    
    return result

print add(X,Y)
print multiply(X,Y)
