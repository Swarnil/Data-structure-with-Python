class SelectionSort():
    def __init__(self):
        self.N=int(input("How Many Elements:"))
        self.A=[]
        for i in range(self.N):
            temp=int(input(f"Enter Element {i+1}: "))
            self.A.append(temp)

    def Process(self):
        for i in range(self.N):
            min=i
            for j in range(i+1,self.N):
                if self.A[min] > self.A[j]:
                    min=j
            self.A[i],self.A[min]=self.A[min],self.A[i]
        print(self.A)

if __name__=='__main__':
    ob=SelectionSort()
    ob.Process()



