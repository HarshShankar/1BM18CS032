#include<bits/stdc++.h>
using namespace std;
void two_largest(vector<int> v1){
    
    make_heap(v1.begin(),v1.end());
    pop_heap(v1.begin(),v1.end());
    v1.pop_back();
    pop_heap(v1.begin(),v1.end());
    v1.pop_back();
    for(auto it=v1.begin();it!=v1.end();it++){
        cout<<*it<<" ";
    }
    cout<<endl;
}
int main()
{
    int n;
    cin>>n;
    while(n--){
        cout<< "\n";
        int k;
        cin>>k;
        vector<int> arr;
        for(int i=0;i<k;i++){
            int ele;
            cin>>ele;
            arr.push_back(ele);
        }
        two_largest(arr);
    }
    return 0;
}