x=int(raw_input())
Multiples=[]
Sum=0
for a in range(1,x):
    if a%3==0:
        Multiples.append(a)
        Sum+=a
    elif a%5==0:
        Multiples.append(a)
        Sum+=a
print Multiples
print Sum

