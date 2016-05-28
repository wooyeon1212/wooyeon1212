a=1
b=2
count=0
def Fibo(a,b):
    c= a+b
    return c
while Fibo(a,b)<4000000:
    print Fibo(a,b)
    if Fibo(a,b)%2==0:
        count=count+Fibo(a,b)
    b=Fibo(a,b)
    a=b-a
    
print count+2
