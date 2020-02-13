import time
import random
import matplotlib.pyplot as plt
def bubble(arr):
        for i in range(len(arr)):
                for j in range(0,len(arr)-1-i):
                        if(arr[j]>arr[j+1]):
                                t=arr[j]
                                arr[j]=arr[j+1]
                                arr[j+1]=t
        return arr
if __name__=="__main__":
        ti=[]
        ite=[i for i in range(100)]
        for i in ite:
                start_time=time.time()
                a=random.sample(range(1,i*1000),i)
                #print(a)
                #print(bubble(a))
                arr=bubble(a)
                timee=(time.time()-start_time)
                print("SECONDS for ", i,"seconds=",timee)
                ti.append(timee)
        plt.plot(ite,ti)
        plt.show()
