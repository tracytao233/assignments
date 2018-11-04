n=eval(input('input a number as a upper range'))
a=[]
a.append(2)
d=[]
for i in range (3,n+1):
    b=0
    c=int(i/2)+1
    for m in a:
        if c>=m:
            d.append(m)
        for j in d:
            if i%j==0:
                break
            else:
                b=b+1
        if b==len(d):
            a.append(i)
print(a)
            
    
