class CQueue:
    def __init__(self,m):
        self.max=m
        self.l=[0] * self.max
        self.front=-1
        self.rear=-1

    def Insert(self):
        if self.front==(self.rear+1)%self.max:
            print("\nSorry! Queue is Full ")
            return
        self.rear=(self.rear+1)%self.max
        # v=(self.rear+1)%self.max
        item=int(input("Enter Item : "))
        # print(self.rear)
        self.l[self.rear]=item
        print(f"{item} Inserted Successfully ")
        if self.front == -1: 
            self.front=0

    def Delete(self):
        if self.front == -1:
            print("\nQueue is Empty !")
            return
        item=self.l[self.front]
        
        print(f"{item} Deleted Successfully ")
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.max
    def Traverse(self):
        if self.front == -1:
            print("\nQueue is Empty !")
            return
        if self.front<self.rear:
            print(self.l[self.front:self.rear+1])
        else:
            print(self.l[self.front:self.max+1] + self.l[:self.rear+1])

if __name__ == '__main__':
        m=int(input("Enter The Size of Queue: "))
        obj = CQueue(m)
        while True:
            print("\n<< ****CIRCULAR QUEUE OPERATION **** >>")
            print("\t\t1.Insert ")
            print("\t\t2.Delete ")
            print("\t\t3.Traverse")
            print("\t\t0.Exit")
            n=int(input("Enter Your Choice: "))
            if n==1:
                obj.Insert()
            if n == 2:
                obj.Delete()
            if n == 3:
                obj.Traverse()
            if n==0:
                break
