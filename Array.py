class array1:
    def __init__(self):
        self.l=[]
        self.max=0
    def createArray(self):
        self.max=int(input("Enter Size of the Array: "))
        print(f"** Enter {self.max} Values **")
        for i in range(self.max):
            v=int(input(f"Enter Value for position[{i + 1}]: "))
            self.l.append(v)
        print("** Array Created Successfully **")

    def showArray(self):
        if (len(self.l))==0:
            print("Sorry! Array is not Created Yet")
            return
        print("Current Values:",self.l)

    def linearSearch(self):
        if (len(self.l))==0:
            print("Sorry! Array is not Created Yet")
            return
        s=int(input("Enter Element for Linear Search: "))
        f=0
        for i in range(self.max):
            if s==self.l[i]:
                f=1
                return i
        if f==0:
            return False
    def Sorting(self):
        if (len(self.l))==0:
            print("Sorry! Array is not Created Yet")
            return
        for i in range(self.max):
            for j in range(i+1,self.max):
                if self.l[i]>self.l[j]:
                    self.l[i],self.l[j]=self.l[j],self.l[i]
        print("Sorted list is: ",self.l)
    def BinarySearch(self):
        if (len(self.l))==0:
            print("Sorry! Array is not Created Yet")
            return
        x = int(input("Enter Element for Binary Search: "))
        low = 0
        high = self.max
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            # If x is greater, ignore left half
            if self.l[mid] < x:
                low = mid + 1
            # If x is smaller, ignore right half
            elif self.l[mid] > x:
                high = mid - 1
            # means x is present at mid
            else:
                return mid
        return False
if __name__=="__main__":
    obj=array1()
    while True:
        print("<<** Data Structure Operation On Array **>>")
        print("\t\t1.Create Array")
        print("\t\t2.Show Array")
        print("\t\t3.Sort Array")
        print("\t\t4.Linear Search")
        print("\t\t5.Binary Search")
        print("\t\t0.Exit")
        n=int(input("Enter Your Choice: "))
        if n==1:
            obj.createArray()
        if n==2:
            obj.showArray()
        if n==3:
            obj.Sorting()
        if n==4:
            print(obj.linearSearch())
        if n==5:
            print(obj.BinarySearch())
        if n==0:
            break

