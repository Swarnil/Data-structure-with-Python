class Stack:
    def __init__(self):
        self.l=[]
        self.top=-1

    def Push(self):
        item =(input("Enter Question: "))
        s=item.split(',')
        for i in range(len(s)):
            print(self.l)
            if s[i] in ('+','-','*','/','^'):
                a=int(self.l.pop(self.top))
                b=int(self.l.pop(self.top-1))
                self.top=self.top-2
                op=s[i]
                if op=='+':
                    self.top += 1
                    self.l.append(b+a)
                if op =='*':
                    self.top += 1

                    self.l.append(b * a)
                if op =='/':
                    self.top += 1
                    self.l.append(b / a)
                if op =='-':
                    self.top += 1
                    self.l.append(b - a)
            else:
                self.top += 1
                self.l.append(int(s[i]))
        print(self.l)

obj = Stack()
obj.Push()
