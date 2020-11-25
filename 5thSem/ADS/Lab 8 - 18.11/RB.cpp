#include <bits/stdc++.h>
using namespace std;

// enum Color {BLACK,RED};

// struct Node{
//     int data;
//     bool color;
//     Node *left, *root, *parent;

//     Node(int data){
//         this->data=data;
//         left=right=parent=NULL;
//         this->color=RED;
//     }
// };

// class RBTree{
//     private:
//         Node *root;
//     protected:
//         void rotateLeft(Node *&, Node *&);
//         void rotateRight(Node *&, Node *&);
//         void fixViolation(Node *&, Node *&);
//     public:
//         RBTree(){
//             root=NULL;
//         }
//         void insert(const int &n);
//         void inorder();
//         void levelOrder();
// };

// void 
int main(){   
    struct kk{
        int a=10;
    };
    kk *k=new kk();
    cout<< &k<<endl;
    int *p=&(k);
    cout<< p<<endl;
    cout<< *p<<endl;
    cout<< &p<<endl;
    cout<< *&p<<endl;
}