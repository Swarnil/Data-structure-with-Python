class BubbleSort():
    def __init__(self):
        self.N=int(input("How Many Elements:"))
        self.A=[]
        for i in range(self.N):
            temp=int(input(f"Enter Element {i+1}: "))
            self.A.append(temp)

    def Process(self):
        for i in range(self.N-1,0,-1):
            for j in range(1,i+1):
                if self.A[j-1] > self.A[j]:
                    self.A[j-1],self.A[j]=self.A[j],self.A[j-1]
        return self.A
if __name__=='__main__':
    ob=BubbleSort()
    print(ob.Process())



