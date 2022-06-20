class node:
    def __init__(self,item):
        self.info=item
        self.link=None
class linkedList:
    def __init__(self):
        self.start=None

#INSERT NODE AT THE LAST POSITION
    def insert_last(self,item):
        n=node(item)
        if self.start==None:
            self.start=n
        else:
            t=self.start
            while t.link!=None:
                t=t.link
            t.link=n
        print(f"\n>> {item} Inserted Successfully At The End")

#INSERT NODE AT THE BEGINNNING 
    def insert_begin(self,item):
        n=node(item)
        print(f"\n>> {item} Inserted Successfully At The Beginning")
        n.link=self.start
        self.start=n

#INSERT NODE AFTER ANY NODE
    def insert_after(self,item,afteritem):
        n=node(item)
        t=self.start
        if self.start==None:
            print("\n>> Empty List !! Insert Some Values First")
            return
        while (t.info != afteritem) and (t.link != None):
            t=t.link
        n.link=t.link
        t.link=n
        if t.info!=afteritem:
            print(f"\n>> {afteritem} Not Found,So {item} Inserted At The End")

        else:    
            print(f"\n>> {item} Inserted Successfully After {afteritem}")
       
#INSERT NODE AT ANY POSITION
    def insert_pos(self,item,pos):
        if pos==0:
            print(">> Position Must Be >=1")
            return
        n = node(item)
        t = self.start
        count = 1
        if self.start==None:
            print("\n>> Empty !! Insert Some Values First")
            return
        while(t.link!= None) and (count < pos-1):
            t = t.link
            count += 1
        if pos-1==count:
            print("\n>> Sorry, Can't Insert At This Position")
            return

        n.link=t.link
        t.link=n
        print(count)

        if pos>count and pos!=count-1:
            print(f"\n>> [{pos}] Position Not Found,So {item} Inserted At The End")
        else:
            print(f"\n>> {item} Inserted Successfully At Position [{pos}]")
       
#DELETE THE FIRST NODE
    def delete_first(self):
        t=self.start
        if t==None:
            print("\n>> Can't Delete, No Element is Present")
        else:
            print(f"\n>> {t.info} Deleted Successfully From Beginning")
            t=t.link
            self.start=t

#DELETE THE LAST NODE              
    def delete_last(self):
        t=self.start
        if t==None:
            print("\n>> Can't Delete, List is Empty !")
        elif t.link==None:
            self.start=None
            print(f"{t.info} Deleted Successfully")
        else:
            while t.link!=None:
                prev=t
                t=t.link
            print(f"{t.info} Deleted Successfully From Last")
            # del(t)
            prev.link=None

 #DELETE ANY NODE BY GIVEN INDEX
    def delete_pos(self, pos):
        if self.start == None:
            print("\n>> Can't Delete, No Element is Present")
            return
        if pos == 0:
            self.start = self.start.link
            print(f"\n>> {self.start.info} Deleted Successfully From Postion [{pos}]")
            return
        else:
            index = 0
            current = self.start
            prev = self.start
            temp = self.start
            f=0
            while(current != None):
                if index == pos:
                    temp = current.link
                    f=1
                    break
                prev = current
                current = current.link
                index += 1
            if f==0:
                print("\n>> Sorry, Position Out of Range")
                return
            prev.link = temp
            print(f"{current.info} Deleted Successfully From Position [{pos}]")
            return 
    
#DELETE ANY PARTICULAR NODE
    def delete_node(self, item):
        if self.start == None:
            print("\n>> Can't Delete, No Element is Present")
            return
        else:
            t = self.start
            if (t != None):
                if (t.info == item):
                    self.start = t.link
                    t = None
                    print(f"\n>> {item} Deleted Successfully")
                    return
            while(t != None):
                if t.info == item:
                    break
                prev = t
                t = t.link
            if(t == None):
                print("\n>> Sorry, Item Not Found")
                return
            prev.link = t.link
            t = None
        print(f"\n>> {item} Deleted Successfully")

#DISPLAY ALL THE NODES
    def traverse(self):
        t=self.start
        if t==None:
            print("\n>> List is Empty")
        else:
            print("\n <<<<<----- List is : ---->>>>>")
            while t!=None:
                print(t.info,end='->')
                t=t.link
#DISPLAY IN REVERSE ORDER
    def ReversePrint(self):
        node = self.start
        values = []
        while node:
            values.append(node.info)
            node = node.link
        for value in reversed(values):
            print(value,end='->')

#SEARCH ANY NODE 
    def search(self,n1):
        t=self.start
        if t==None:
            print("\n>> Sorry , The List is Empty !")
            return
        elif n1==t.info:
            print(f"\n>> {n1} Fount At The Position [0] ")
            return
        else:
            count=0
            f=0
            while(t.link!=None):
                count+=1
                t=t.link
                if t.info==n1:
                    f=1
                    break
            if f==0:
                print("\n>> Sorry , Item Not Found !")
            else:
                print(f"\n>> {n1} Fount at the position {count} ")

#COUNT TOTAL NUMBER OF NODES  
    def node_count(self):
        t=self.start
        if t==None:
            print("\n>> Sorry, There Is No Node !")
        else:
            count=0
            while(t!=None):
                count+=1
                t=t.link
            print("\n>> Number of Nodes :",count)
        
#MAIN FUNCTION TO CALL ALL THE FUNCTIONS
if __name__ == '__main__':
    obj=linkedList()
    print("\n\t<< *** SINGLE LINKED LIST OPERATION *** >>")
    while True:
        print("\n <<-- INSERTION -->>")
        print("\t 1.Insert At Beginning")
        print("\t 2.Insert At Last")
        print("\t 3.Insert After Specific Item")
        print("\t 4.Insert At Specific Position")

        print("\n <<-- DELETION -->>")
        print("\t 5.Delete From First")
        print("\t 6.Delete From Last")
        print("\t 7.Delete Specific Item")
        print("\t 8.Delete Specific Position")

        print("\n <<-- TRAVERSION -->>")
        print("\t 10.Traverse")
        print("\t 11.Traverse Reverse")
        print("\t 12.Search Any Item")
        print("\t 13.Node Counter")

        print("\t 0.Exit")
        m=int(input("Enter Your Choice: "))
        if m==1:
            n1=int(input("Enter The Item: "))
            obj.insert_begin(n1)
        elif m==2:
            n1=int(input("Enter The Item: "))
            obj.insert_last(n1)
        elif m==3:
            n1=int(input("Enter The Item: "))
            afteritem=int(input("After Which Item You Want To Insert: "))
            obj.insert_after(n1,afteritem)
        elif m==4:
            n1=int(input("Enter The Item: "))
            pos=int(input("Enter Position: "))
            obj.insert_pos(n1,pos)
        elif m==5:
            obj.delete_first()
        elif m==6:
            obj.delete_last()
        elif m==7:
            n1=int(input("Enter The Item To Be Deleted: "))
            obj.delete_node(n1)
        elif m==8:
            n1=int(input("Enter The Position To Be Deleted: "))
            obj.delete_pos(n1)
        elif m==10:
            obj.traverse()
        elif m==11:
            obj.ReversePrint()
        elif m==12:
            n1=int(input("Enter The Item To Be Searched: "))
            obj.search(n1)
        elif m==13:
            obj.node_count()
       
        elif m==0:
            break
        else:
            print("\n>> Sorry, Invalid Input")
    