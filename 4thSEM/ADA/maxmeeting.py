def max(s,f):
    n=len(f)
    pos=[i for i in range(1,n+1)]
    for i in range(n):
        for j in range(n-1-i):
            if (f[j]>f[j+1]):
                tempf=f[j]
                temps=s[j]
                tempn=pos[j]
                f[j]=f[j+1]
                s[j]=s[j+1]
                pos[j]=pos[j+1]
                f[j+1]=tempf
                s[j+1]=temps
                pos[j+1]=tempn
    happening=[]
    time_limit=f[0]
    happening.append(pos[0])
    for i in range(1,n):
        if(s[i]>time_limit):
            happening.append(pos[i])
            time_limit=f[i]
    return happening

s=[1,3,0,5,8,5]
f=[2,4,6,7,9,9]
print(max(s,f))

