#include<iostream>
using namespace std;
class BTreeNode
{
    int *keys;
    int t;
    BTreeNode **C;
    int n;
    bool leaf;

    public:
        BTreeNode(int _t, bool _leaf);
        
        void insertNonFull(int k);
        
        void splitChild(int i,BTreeNode *y);
        
        void traverse();
        
        BTreeNode *search(int k);

friend class BTree;
};

class BTree{
    BTreeNode *root;
    int t;

    public:

        BTree(int _t)
        {
            root=NULL;
            t=_t;
        }

        void traverse(){
            if(root!=NULL) root->traverse();
        }

        BTreeNode* search(int k){
            return (root==NULL)? NULL : root->search(k);
        }
        
        void insert(int k);
};

BTreeNode::BTreeNode(int tt, bool leaff){
    t=tt;
    leaf=leaff;

    keys= new int[2*tt-1];
    C=new BTreeNode *[2*t];

    n=0;
}

void BTreeNode::traverse(){
    
    int i;
    for (i=0;i<n;i++){
    
        if(leaf==false)
            C[i]->traverse();
        
        cout<<" "<< keys[i];
    }
    if(leaf==false){
        C[i]->traverse();
    }
}

BTreeNode *BTreeNode::search(int k){
    int i=0;
    while(i<n and k>keys[i])
        i++;
    
    if(keys[i]==k) return this;

    if(leaf == true) return NULL;

    return C[i]->search(k);
}

void BTree::insert(int k)
{
    if (root == NULL){
        root=new BTreeNode(t,true);
        root->keys[0]=k;
        root->n=1;
    }
    else{
        if(root->n == 2*t-1){
            BTreeNode *s=new BTreeNode(t,false);
            s->C[0]=root;
            s->splitChild(0,root);
            int i=0;
            if(s->keys[i]<k) i++;
            s->C[i]->insertNonFull(k);

            root=s;
        }
        else{
            root->insertNonFull(k);
        }
    }
}

void BTreeNode::insertNonFull(int k){
    int i=n-1;

    if(leaf == true){
        while(i>=0 and keys[i]>k)
        {
            keys[i+1]=keys[i];
            i--;
        }
        keys[i+1]=k;
        n=n+1;
    }
    else{
        while(i>=0 and keys[i]>k)
        i--;
        
        if(C[i+1]->n == 2*t-1)
        {
            splitChild(i+1,C[i+1]);
            if(keys[i+1]<k)
                i++;
        }
        C[i+1]->insertNonFull(k);
    }
}
void BTreeNode::splitChild(int i,BTreeNode *y){
    BTreeNode *z=new BTreeNode(y->t,y->leaf);
    z->n=t-1;
    for (int j=0; j<t-1; j++)
        z->keys[j]=y->keys[j+t];
    
    if(y->leaf == false){
        for(int j=0;j<t;t++)
            z->C[j]=y->C[j+1];
    }
    y->n=t-1;

    for(int j =n;j>=i+1;j++){
        C[j+1]=C[j];
    }
    C[i+1]=z;

    for (int j= n-1;j>=1;j--)
        keys[j+1]=keys[j];
    
    keys[i]=y->keys[t-1];
    n=n+1;
}

int main(){
    int tt;
    cout<< "Enter B Tree's minimum capacity:";
    cin>>tt;
    BTree t(tt);

    int k,ele;
    cout<<"Number of elements to insert:";
    cin>>k;

    cout<<"Enter the elements \n";
    while (k--) {
        cin >> ele;
        t.insert(ele);
    }

    cout << "The B-tree is: ";
    {
        // * In a different block because it doesn't end with a newline
        t.traverse();
        cout << endl;
    }
}