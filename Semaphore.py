class Semaphore:
    def __init__(self,mutex,full,empty,count):
        self.mutex=mutex
        self.full=full
        self.empty=empty
        self.count=0
        
    def Producer(self):
        self.mutex-=1
        self.full+=1
        self.empty-=1
        self.count+=1
        print(f"\n>>Producer Produces -> {self.count}")
        self.mutex+=1

    def Consumer(self):
        self.mutex-=1
        self.full-=1
        self.empty+=1
        print(f"\n>>Consumer Consumes-> {self.count}")
        self.count-=1
        self.mutex+=1

if __name__=='__main__':
    mutex=1
    full=0
    empty=int(input("How Many Slots: "))
    ob=Semaphore(mutex,full,empty)

    print("\n<<*** PRODUCER CONSUMER PROBLEM ***>>")
    print("\t1. Producer")
    print("\t2. Consumer")
    print("\t3. Exit")
    while True:
        n=int(input("Enter Your Choice: "))
        if n==1:
            if mutex==1 and empty!=0:
                ob.Producer()
            else:
                print("\n-->> Sorry Slot is Full")
        
        elif n==2:
            if mutex==1 and full!=0:
                ob.Consumer()
            else:
                print("\n-->> Sorry Slot is Empty")
        elif n==0:
            break

