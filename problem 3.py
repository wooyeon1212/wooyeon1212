x=int(raw_input())
factors=list()
for a in range(1,x):
    if x%a==0:
        factors.append(a)
print factors
print len(factors)
length=len(factors)
def prime(num):
    primeNums=list()
    primeNums.append(1)
    primeNums.append(num)
    return primeNums
b=0
D=1
while b<length:
    F=list()
    while factors[b]>=D:
        if factors[b]%D==0:
            F.append(D)
        print F
        D+=1
    
        
        

    
            

