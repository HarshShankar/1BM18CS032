def first(arr,beg,end,x):
    if(beg<=end):
        mid=(beg+end)//2
        if((mid==0 or arr[mid-1]<x)and arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            return first(arr,mid+1,end,x)
        else:
            return first(arr,beg,mid-1,x)
    else:
        return -1

def last(arr,beg,end,x):
    if(beg<=end):
        mid=(beg+end)//2
        if((x==end or arr[mid+1]>x) and arr[mid]==x):
            return mid
        elif(x<arr[mid]):
            return last(arr,beg,mid-1,x)
        else:
            return last(arr,mid+1,end,x)
    else:
        return -1

ar=[1,2,2,2,2,3,4,5]
fir=first(ar,0,len(ar)-1,2)
las=last(ar,0,len(ar)-1,2)
if(fir!=-1):
    print("first occurence=",fir,"\nlast occurence=",las)
else:
    print("Element not found")
