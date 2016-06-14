#-*- coding: utf-8 -*-
#지뢰 찾기 리스트를 생성하여 지뢰를 랜덤하게 배설하는 프로그램을 설계했습니다
import random

def printMatrix(_list):
    for row in _list:
        print ("   ".join(row))

def randomBomb():
    bomb=['*','.']
    return random.choice(bomb)

m = int(input('colum: ')) 
n = int(input('row: '))

n_matrix = []

for ndx in range(0,n):
    n_matrix.append(["*"] * m)


for ndx in range(0,n):
    for mdx in range(0,m):
            n_matrix[ndx][mdx]=randomBomb()

for ndx in range(0,n):
    for mdx in range(0,m):
            if n_matrix[ndx][mdx] != "*":
                bombCount = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        xindex = ndx + x
                        yindex = mdx + y
                        if xindex > -1 and yindex > -1 and xindex < m  and yindex < n:
                            if "*" == n_matrix[ndx + x][mdx + y]:
                                bombCount = bombCount + 1

                n_matrix[ndx][mdx]=str(bombCount)

printMatrix(n_matrix)
