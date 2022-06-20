class node:
    def __init__(self,item):
        self.info=item
        self.link=None
class linkedList:
    def __init__(self):
        self.start=None

#INSERT NODE AT THE LAST POSITION
    def insert_last(self,item):
        n=node(item)
        if self.start==None:
            self.start=n
        else:
            t=self.start
            while t.link!=None:
                t=t.link
            t.link=n
        print(f"\n>> {item} Inserted Successfully At The End")
#DISPLAY ALL THE NODES
    def traverse(self):
        t=self.start
        if t==None:
            print("\n>> List is Empty")
        else:
            print("\n <<<<<----- List is : ---->>>>>")
            while t!=None:
                print(t.info,end='->')
                t=t.link
#Display Node In Reverse Order
    def PrintRev(self):
        top=-1
        list=[]
        t=self.start
        if t==None:
            print("Sorry List is Empty")
            return
        while t!=None:
            top+=1
            list.append(t.info)
            t=t.link
        while top!=-1:
            g=list.pop(top)
            print(g,end='->')
            top-=1

#Reverse the original linked list
    def ListRev(self):
    # initialize variables
        previous = None         
        current = self.start     
        following = current.link    
        while current:
            current.link = previous 
            previous = current      
            current = following       
            if following:              
                following = following.link   
        self.start = previous
if __name__ == '__main__':
    obj=linkedList()
    while True:
        print("\n\t 1.Insert At Last")
        print("\t 10.Traverse")
        print("\t 11.Traverse Reverse")
        print("\t 12.Linked List Reverse")
        print("\t 0.Exit")
        m=int(input("Enter Your Choice: "))
        if m==1:
            n1=int(input("Enter The Item: "))   
            obj.insert_last(n1)    
        elif m==10:
            obj.traverse()
        elif m==11:
            obj.PrintRev()
        elif m==12:
            obj.ListRev()
        elif m==0:
            break
        else:
            print("\n>> Sorry, Invalid Input")
    