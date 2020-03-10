def bubble(arr):
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr)-i-1):
            if (arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

if __name__=="__main__":
    a=list(map(int,input("Enter the numbers").strip().split()))
    a=bubble(a)
    k=int(input("Enter the value of K"))
    n=len(a)
    for i in range(n,n-k,-1):
        print(i)
