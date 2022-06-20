class stack:
    def __init__(self, max):
        self.max = max
        self.arr = []
        self.top = -1
    
    def traverse(self):
        return self.arr
    
    def push(self, item):
        if self.top == self.max - 1:
            print ("full")
            return
        else:
            self.top += 1
            self.arr.append(item)
            
    def pop(self):
        if self.top == -1:
            print("empty")
            return
        else:
            self.arr.pop(self.top)
            self.top -= 1

ob = stack(3)
ob.push(10)
ob.push(20)
ob.push(30)
ob.traverse()
ob.pop()
ob.traverse()