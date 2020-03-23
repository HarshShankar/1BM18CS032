def median(a,b):
    if(len(a)!=1 and len(b)!=1):
        m1=len(a)//2
        m2=len(b)//2
        if(m1<m2):
            return median(a[m1:],b[:m2])
        elif(m2<m1):
            return median(a[:m1],b[m2:])
        else:
            return ((a[m1]+b[m2])//2)
    else:
            return ((a[m1]+b[m2])//2)

a=[1,3,7,9,10,11]
b=[24,27,30,32,33]
print(median(a,b))
