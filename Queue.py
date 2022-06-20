class Queue:
    def __init__(self,m):
        self.max=m
        self.l=[0] * self.max
        self.front=-1
        self.rear=-1

    def Insert(self):
        if self.rear==self.max-1:
            print("\nSorry! Queue is Full ")
            return
        self.rear+=1
        v=self.rear+1
        item=int(input(f"Enter Item {v}: "))
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
            self.front=self.front+1

    def Traverse(self):
        if self.front == -1:
            print("\nQueue is Empty !")
            return
        print(self.l[self.front:self.rear+1])

if __name__ == '__main__':
        m=int(input("Enter The Size of Queue: "))
        obj = Queue(m)
        while True:
            print("\n<< **** QUEUE OPERATION **** >>")
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

    