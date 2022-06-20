class node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,k):
        n=node(k)
        if self.root==None:
            self.root=n
            return
        t=self.root
        while(t!=None):
            prev=t
            if n.key<=t.key:
                t=t.left
            else:
                t=t.right
        if n.key<=prev.key:
            prev.left=n
        else:
            prev.right=n
    def Preorder(self,R):
        if R!=None:
            print(R.key,end=" ")
            ob.Preorder(R.left)
            ob.Preorder(R.right)
    def Inorder(self,R):
            if R!=None:
                ob.Inorder(R.left)
                print(R.key,end=" ")
                ob.Inorder(R.right)
    def Postorder(self,R):
            if R!=None:
                ob.Postorder(R.left)
                ob.Postorder(R.right)
                print(R.key,end=" ")

if __name__=='__main__':     
    ob=BST()
    print("-->> BINARY SEARCH TREE <<--")
    while True:
        print("\n\t1. Insert Node")
        print("\t2. Delete Note")
        print("\t3. Pre-Order Traversal")
        print("\t4. In-Order Traversal")
        print("\t5. Post-Order Traversal")
        print("\t0. Exit")

        n=int(input("Enter Your Choice:"))
        if n==1:
            k=int(input("Enter The Key: "))
            ob.insert(k)
        elif n==2:
            pass
        elif n==3:
            print("\nPreorder Traversal:")
            ob.Preorder(ob.root)
        elif n==4:
            print("\nInorder Traversal:")
            ob.Inorder(ob.root)
        elif n==5:
            print("\nPostorder Traversal:")
            ob.Postorder(ob.root)
        elif n==0:
            break
        else:
            print("Sorry, Invalid Input")
