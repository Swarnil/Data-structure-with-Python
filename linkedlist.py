class node:
    def __init__(self, item):
        self.data = item
        self.next = None

class linkedlist:
    def __init__(self, item):
        self.start = node(item)

    def traverse(self):
        if self.start == None:
            print("List has no elements")
            return
        t = self.start
        while t != None:
            print(t.data , end = "")
            t = t.next

    def insertBegining(self,item):
        if self.start == None:
            print("List has no elements")
            return
        n = node(item)
        n.next = self.start
        self.start = n

    def insertEnd(self,item):
        if self.start == None:
            print("List has no elements")
            return
        n = node(item)
        t = self.start
        while t.next != None:
            t = t.next
        t.next = n
    
    def insertSpecified(self,item,index):
        if self.start == None:
            print("List has no elements")
            return
        n = node(item)
        t = self.start
        pos = 1
        while pos < index-1 and t != None:
            t = t.next
            pos += 1
        n.next = t.next
        t.next = n
    
    def deleteStart(self):
        if self.start == None:
            print("List has no elements")
            return
        t = self.start
        self.start = t.next
        del(t)

        
        

ob = linkedlist(20)
ob.traverse()
ob.insertBegining(10)
ob.traverse()
ob.insertEnd(30)
ob.traverse()
ob.insertSpecified(40,2)
ob.traverse()
ob.deleteStart()
ob.traverse()