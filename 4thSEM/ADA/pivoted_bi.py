def binary(arr,beg,end,x):
    if(beg<=end):
        mid=(beg+end)//2
        if(x==arr[mid]):
            return mid 
        elif(x > arr[mid]):
            binary(arr,mid+1,end,x)
        else:
            binary(arr,0,mid-1,x)
    else:
        return -1
    
def pivot(arr,x):
    pivot=0
    for i in range(0,len(arr)-2):
        if arr[i]>arr[i+1]:
            pivot=i
    if(x>arr[0]):
        return (binary(arr,0,pivot,x))
    else:
       return (binary(arr,pivot+1,len(arr)-1,x))

if __name__=="__main__":
    arr=list(map(int,input("Enter the elements of the array \n").strip().split()))
    x=int(input("Enter the element to be found in the array \n"))
    pos=pivot(arr,x)
    print (("Element found at ",pos) if pos!=-1 else "Element not found")
