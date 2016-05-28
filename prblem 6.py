Sum=0
for a in range(1,101):
    b=a**2
    Sum+=b
 
Sum2=0
for a in range(1,101):
    Sum2+=a

realSum=Sum2**2-Sum
print realSum
