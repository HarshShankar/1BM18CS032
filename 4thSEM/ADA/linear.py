def linear(arr,i,x):
        if(i==len(arr)):
                return -1
        if(arr[i]==x):
                return i
        return linear(arr,i+1,x)
        
        
a=[1,2,3,4,5]
print(linear(a,0,4))
