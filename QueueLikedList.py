class node:
    def __init__(self,item):
        self.info=item
        self.link=None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def Insert(self,item):
        n=node(item)
        if self.front == None:
            self.front=n
            self.rear=n
            print(f"{item} Inserted Successfully")
        else:
            self.rear.link=n
            self.rear=n
            print(f"{item} Inserted Successfully")
    def Delete(self):
        if self.front == None and self.rear==None:
            print("Sorry No Item to Delete")
            return
        item=self.front.info
        if self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.front = self.front.link
            print(f"{item} Deleted Successfully")
        
    def Traverse(self):
        if self.front == None and self.rear==None:
            print("Empty")

        else:
            t=self.front
            while(t!=None):
                print(t.info,end=" ")
                t=t.link

if __name__ == '__main__':
        # m=int(input("Enter The Size of Queue: "))
        obj = Queue()
        while True:
            print("\n<< **** QUEUE OPERATION **** >>")
            print("\t\t1.Insert ")
            print("\t\t2.Delete ")
            print("\t\t3.Traverse")
            print("\t\t0.Exit")
            n=int(input("Enter Your Choice: "))
            if n==1:
                n1=int(input("Enter The Item: "))
                obj.Insert(n1)
            if n == 2:
                obj.Delete()
            if n == 3:
                obj.Traverse()
            if n==0:
                break

    