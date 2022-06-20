
class node:
    def __init__(self,item):
        self.info=item
        self.link=None

class CLinkedList:
    def __init__(self):
        self.start=None

    def insert_begin(self,item):
        n=node(item)
        if self.start==None:
            self.start=n
            self.start.link=self.start
        else:
            t=self.start
            while t.link!=self.start:
                t=t.link
            t.link=n
            n.link=self.start
            self.start=n

    def insert_last(self,item):
        n=node(item)
        if self.start==None:
            self.start=n
            self.start.link=self.start
        else:
            t=self.start
            while(t.link != self.start):
                t=t.link
            t.link=n
            n.link=self.start

    def delete_last(self):
        if self.start==None:
            print("Sorry List is Empty")
            return
        t=self.start
        if t.link==t:
            self.start=None
            del(t)
            return
        while t.link!=self.start:
            prev=t
            t=t.link
        del(t)
        prev.link=self.start

    def delete_first(self):
        if self.start==None:
            print("Sorry List is Empty")
            return

        if self.start.link==self.start:
            self.start=None
            return
     
        prev=self.start
        t=self.start
        while t.link!=self.start:
            t=t.link
        self.start=self.start.link
        t.link=self.start
        del(prev)

    def traverse(self):
        t=self.start
        if t==None:
            print("Sorry List is Empty")
            return
        while (t.link!=self.start):
            print(t.info,end="->")
            t=t.link
        print(t.info)

    def ReversePrint(self):
        top=-1
        list=[]
        t=self.start
        if t==None:
            print("Sorry List is Empty")
            return
        while t.link!=self.start:
            top+=1
            list.append(t.info)
            t=t.link
        list.append(t.info)
        top+=1
        while top!=-1:
            g=list.pop(top)
            print(g,end='->')
            top-=1

if __name__ == '__main__':
    obj=CLinkedList()
    print("\n\t<< *** CIRCULAR LINKED LIST OPERATION *** >>")
    while True:
        print("\n <<-- INSERTION -->>")
        print("\t 1.Insert At Beginning")
        print("\t 2.Insert At Last")
  
        print("\n <<-- DELETION -->>")
        print("\t 3.Delete From First")
        print("\t 4.Delete From Last")
    
        print("\n <<-- TRAVERSION -->>")
        print("\t 5.Traverse")
        print("\t 6.Traverse Reverse")

        print("\t 0.Exit")
        m=int(input("Enter Your Choice: "))
        if m==1:
            n1=int(input("Enter The Item: "))
            obj.insert_begin(n1)
        elif m==2:
            n1=int(input("Enter The Item: "))
            obj.insert_last(n1)

        elif m==3:
            obj.delete_first()
        elif m==4:
            obj.delete_last()

        elif m==5:
            obj.traverse()
        elif m==6:
            obj.ReversePrint()
 

 
        elif m==0:
            break
        else:
            print("\n>> Sorry, Invalid Input")
