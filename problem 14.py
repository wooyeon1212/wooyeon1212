#a= start num

def Collatz(a):
    
    Col=list()
    Col.append(a)
    while a!=1:
        if a%2==0:
            a=a/2
            Col.append(a)
        else :
            a=3*a+1
            Col.append(a)
    return len(Col)


n=2
Answer=Collatz(2)
while n<1000000:
    if Answer<Collatz(n):
        Answer=Collatz(n)
        answer=n
    
        
    n=n+1
    
print answer
