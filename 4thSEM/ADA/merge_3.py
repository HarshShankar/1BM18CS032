def merge(arr):
    if(len(arr)>2):
        mid1=len(arr)//3
        mid2=(2*(len(arr)))//3
        # print(mid1,mid2)
        L1=arr[:mid1]
        L2=arr[mid1:mid2]
        L3=arr[mid2:]
        merge(L1)
        merge(L2)
        merge(L3)
        i=j=k=0
        p=0
        while(i<len(L1) and j<len(L2) and k<len(L3)):
            if(L1[i]<L2[j]):
                if(L1[i]<L3[k]):
                    arr[p]=L1[i]
                    p+=1
                    i+=1
                else:
                    arr[p]=L3[k]
                    p+=1
                    k+=1
            else:
                if(L2[j] < L1[i]):
                    if(L2[j]<L3[k]):
                        arr[p]=L2[j]
                        p+=1
                        j+=1
                    else:
                        arr[p]=L3[k]
                        k+=1
                        p+=1
        while(i<len(L1) and j<len(L2)):
            if(L1[i]<L2[j]):
                arr[p]=L1[i]
                i+=1
            else:
                arr[p]=L2[j]
                j+=1
            p+=1
        while(j<len(L2) and k<len(L3)):
            if(L2[j] < L3[k]):
                arr[p]=L2[j]
                j+=1
            else:
                arr[p]=L3[k]
                k+=1
            p+=1
        while(i<len(L1)):
            arr[p]=L1[i]
            i+=1
            p+=1
        while(j<len(L2)):
            arr[p]=L2[j]
            j+=1
            p+=1
        while(k<len(L3)):
            arr[p]=L3[k]
            k+=1
            p+=1
    else:
        if(len(arr)==2):
            if(arr[1]<arr[0]):
                arr[1],arr[0]=arr[0],arr[1]
if __name__=="__main__":
    n=int(input("Enter the number of elements: "))
    g=list(map(int,(input("\nEnter the elements: ").strip().split())))[:n]
    merge(g)
    print("Sorted array :",g)
