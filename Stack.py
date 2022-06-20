class Stack:
    def __init__(self,m):
        self.max=m
        self.l=[]
        self.top=-1
    def Push(self):
        if self.top==self.max-1:
            print(">> Stack Overflow")
            return
        item = int(input("Enter Item: "))
        self.top+=1
        self.l.append(item)
        print(">> ",item,"Is Inserted"
                         " to Stack")
        print(self.l)
    def Pop(self):
        if self.top == -1:
            print(">> Stack is Empty")
            return
        item=self.l.pop(self.top)
        self.top-=1
        print(">> ", item, "Is Deleted From Stack")
        print(self.l)
    def Display(self):
        if self.top == -1:
            print(">> Stack is Empty")
            return
        print(self.l)
m=int(input("Enter The Size of Stack: "))
obj = Stack(m)
while True:
    print("<< **** STACK OPERATION **** >>")
    print("\t\t1.Push ")
    print("\t\t2.Pop ")
    print("\t\t3.Display")
    print("\t\t0.Exit")
    n=int(input("Enter Your Choice: "))
    if n==1:
        obj.Push()
    if n == 2:
        obj.Pop()
    if n == 3:
        obj.Display()
    if n==0:
        break