class Student:
    def __init__(self):
        self.name=input("Enter Name: ")
        self.roll=int(input("Enter Roll: "))
        self.marks = int(input("Enter Marks:"))
    def showData(self):
        print("Name is: ",self.name)
        print("Roll is: ",self.roll)
    def showMarks(self):
        print("Marks is: ",self.marks)
obj=Student()
obj.showData()
obj.showMarks()
