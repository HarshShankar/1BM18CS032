#include<bits/stdc++.h>
using namespace std;

void uniq(int l,int r){
    vector <int> res;
    for(int i=l;i <= r;i++){
        int num= abs(i);
        bool visited[10]= {false};
        while(num){
            if (visited[num%10])
                break;
            visited[num%10]=true;
            num=num/10;
        }
        if(num ==0)
            cout<<i<<" ";
    }
}
int main(){
    int l,r;
    cout<<"L :"<<endl;
    cin>>l;
    cout<<"R "<<endl;
    cin>>r;

    uniq(l,r);
}