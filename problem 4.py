product=list()
a=100
while a<1000:
    for b in range(100,1000):
        product.append(a*b)
    a+=1

palindrome=list()
for x in range(0,len(product)):
    if str(product[x])==str(product[x])[::-1]:
        palindrome.append(product[x])
palindrome.sort()
print palindrome[-1]
        
