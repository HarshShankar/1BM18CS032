#include <bits/stdc++.h>

using namespace std;

class Node{
    public:
        int key;
        Node **forward;
        Node (int,int);
};
Node::Node(int key,int level){
    this->key=key;
    forward=new Node*[level+1];
    memset(forward,0,sizeof(Node*)*(level+1));
}
class SkipList{
    public:
        int MAXLVL;
        float p;
        int level;
        Node* header;
        SkipList(int maxlvl,float p);
        int randomlevel();
        Node* createNode(int,int);
        void insertElement(int);
        void searchElement(int);
        void deleteElement(int);
        void displayList();
};

SkipList::SkipList(int maxlvl,float pp){
    this->MAXLVL=maxlvl;
    this->p=pp;
    level=0;
    header=new Node(-1,MAXLVL);
};
Node* SkipList::createNode(int key,int level){
    Node *n=new Node(key,level);
    return n;
};
int SkipList::randomlevel(){
    float r=(float)rand()/RAND_MAX;
    int lvl=0;
    while(r<p && lvl<MAXLVL)
    {
        lvl++;
        r=(float)rand()/RAND_MAX;
    }
    return lvl;
};
void SkipList::insertElement(int key){
    Node* current=header;
    Node* update[MAXLVL+1];
    memset(update,0,sizeof(Node*)*(MAXLVL+1));

    for(int i= level;i>=0;i--)
    {
        while(current->forward[i] != NULL && current->forward[i]->key<key)
            current=current->forward[i];
        update[i]=current;
    }
    current=current->forward[0];
    if(current == NULL || current->key != key)
    {
        int rlevel = randomlevel();
        if(rlevel>level)
        {
            for(int i=level+1;i<rlevel+1;i++)
                update[i]=header;
            level= rlevel;
        }

        Node* n=createNode(key,rlevel);

        for(int i=0;i<=rlevel;i++)
        {
            n->forward[i]=update[i]->forward[i];
            update[i]->forward[i]=n;
        }
        cout << "Successfully Inserted key" << key << "\n";
    }
};
void SkipList::searchElement(int key){
    Node *current=header;
    for(int i=level;i>=0;i--){
        while (current->forward[i]->key<key && current->forward[i])
            current=current->forward[i];
    }
    current=current->forward[0];
    if(current and current->key==key)
        cout<<("Element found")<<endl;
        return;
    cout<<"Element not found"<<endl;
}
void SkipList::deleteElement(int key){
    Node* current=header;
    for(int i=level;i>=0;i--){
        while(current->forward[i]!=NULL && current->forward[i]->key<key){
            current=current->forward[i];
        }
        if(current->forward[i]->key==key && current->forward[i]){
            for(int j=i;j>=0;j--){
                current->forward[i]=current->forward[i]->forward[i];
            }
            while(level>=0 && header->forward[level]==0)
                level--;
            cout<<"Succesfully deleted key"<<endl;
            return;
        }
    }
    cout<<"Element isn't present in the list"<<endl;
    return;

}
void SkipList::displayList()
{
    cout<<"Skip List";
    for(int i=0;i<=level;i++){
        Node* node=header->forward[i];
        cout<<"Level"<<i<<": ";
        while(node != NULL){
            cout<<node->key<<" ";
            node=node->forward[i];
        }
        cout<<"\n";
    }
};

int main()
{
    srand((unsigned)time(0));

    SkipList lst(3,0.5);
    lst.insertElement(3); 
	lst.insertElement(6); 
	lst.insertElement(7); 
	lst.insertElement(9); 
	lst.insertElement(12); 
	lst.insertElement(19); 
	lst.insertElement(17); 
	lst.insertElement(26); 
	lst.insertElement(21); 
	lst.insertElement(25); 
	lst.displayList(); 
    lst.searchElement(21);
    lst.deleteElement(21);
}

