def first(a,beg,end,key):
	if(beg<=end):
		mid=(beg+end)/2
		if((mid==0 or x > a[mid-1]) and x==a[mid]):
			return mid
		elif(x>a[mid]):
			return first(a,mid+1,end,key)
		else:
			return first(a,beg,mid-1,key)
	return -1
	
def last(a,beg,end,key):
	if(beg<=end):
		mid=(beg+end)/2
		if((mid== len(arr)-1 or x < a[mid-1]) and x==a[mid]):
			return mid
		elif(x < a[mid]):
			return first(a,beg,mid+1,key)
		else:
			return first(a,mid+1,end,key)
	return -1

	
	
arr=[1,1,1,4,5]
binary(arr,0,len(arr)-1,1)			 
