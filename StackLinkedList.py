class node:
    def __init__(self,item):
        self.info=item
        self.link=None
class linkedList:
    def __init__(self):
        self.start=None
        self.top=-1

#INSERT NODE AT THE LAST POSITION
    def insert_last(self,item):
        n=node(item)
        if self.top==-1:
            self.start=n
            self.top+=1
        else:
            t=self.start
            while t.link!=None:
                t=t.link
            t.link=n
            self.top+=1
        print(f"\n>> {item} Inserted Successfully into thre Stack")

#DELETE THE LAST NODE              
    def delete_last(self):
        t=self.start
        if self.top==-1:
            print("\n>> Can't Delete, Stack is Empty !")
        elif self.top==0:
            self.start=None
            print(f"{t.info} Deleted Successfully")
            self.top-=1
        else:
            while t.link!=None:
                prev=t
                t=t.link
            print(f"{t.info} Deleted Successfully From Last")
            # del(t)
            prev.link=None
            self.top-=1

#DISPLAY ALL THE NODES
    def traverse(self):
        t=self.start
        if self.top==-1:
            print("\n>> Stack is Empty")
        else:
            print("\n <<<<<----- Stack is : ---->>>>>")
            while t!=None:
                print(t.info,end='->')
                t=t.link

obj = linkedList()
while True:
    print("<< **** STACK OPERATION **** >>")
    print("\t\t1.Push ")
    print("\t\t2.Pop ")
    print("\t\t3.Display")
    print("\t\t0.Exit")
    n=int(input("Enter Your Choice: "))
    if n==1:
        n1=int(input("Enter The Item: "))
        obj.insert_last(n1)
    if n == 2:
        obj.delete_last()
    if n == 3:
        obj.traverse()
    if n==0:
        break