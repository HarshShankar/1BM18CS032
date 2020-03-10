
def insert(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j=j-1
        
        a[j+1]=key


arr = [10,9,8,7,6,5,4,3,2,1] 
insert(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 
