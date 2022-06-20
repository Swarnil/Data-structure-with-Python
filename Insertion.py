class SelectionSort():
    def __init__(self):
        self.N=int(input("How Many Elements:"))
        self.A=[]
        for i in range(self.N):
            temp=int(input(f"Enter Element {i+1}: "))
            self.A.append(temp)

    def Process(self):
        for i in range(1, len(self.A)):
            key = self.A[i]
            j = i-1
            while j >= 0 and key < self.A[j] :
                    self.A[j + 1] = self.A[j]
                    j -= 1
            self.A[j + 1] = key
        return self.A
if __name__=='__main__':
    ob=SelectionSort()
    print(ob.Process())