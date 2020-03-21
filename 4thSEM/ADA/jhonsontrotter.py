from math import factorial

class JT:
    def __init__(self):
        self.RtoL=True
        self.LtoR=False

    def Getmobile(self,a,dir):
        mobile=0
        mobile_prev=0
        for i in range(len(a)):
            if(dir[a[i]-1]==self.RtoL and i!=0):
                if(a[i]>a[i-1] and a[i]>mobile_prev):
                    mobile=a[i]
                    mobile_prev=a[i]
            if(dir[a[i]-1]==self.LtoR and i<(len(a)-1)):
                if(a[i]>a[i+1] and a[i]>mobile_prev):
                    mobile=a[i]
                    mobile_prev=a[i]
        if(mobile==0 and mobile_prev==0):
            return 0
        else:
            return mobile
    def searchArr(self,a,mobile):
        for i in range(len(a)):
            if(a[i]== mobile):
                return i+1
    def Oneperm(self,a,dir):
        mobile=self.Getmobile(a,dir)
        pos=self.searchArr(a,mobile)
        if(dir[a[pos-1]-1]==self.RtoL):
            a[pos-1],a[pos-2]=a[pos-2],a[pos-1]
        elif(dir[a[pos-1]-1]==self.LtoR):
            a[pos-1],a[pos]=a[pos],a[pos-1]
        for i in range(len(a)):
            if(a[i]>mobile):
                dir[a[i]-1]=not(dir[a[i]-1])
        print(a)
    def perprint(self,n):
        a=[i+1 for i in range(n)]
        dir=[True for i in range(n)]
        print(a)
        for i in range(factorial(n)-1):
            self.Oneperm(a,dir)
jt=JT()
jt.perprint(4)


