def Process(n,arr,t):
    # print("####")
    count=0
    wt=[]
    i=0
    while(i<n):
        if(arr[i]<=t):
            count=count+arr[i]
            wt.append(count)
            i+=1
        else:
            count=count+t
            wt.append(count)
            temp=arr[i]-t
            i=+1
    wt.append(temp+count)
    print(wt)
arr=[]
n=int(input("How Many Process:"))
for i in range(n):
    g=int(input(f"Enter Burst Time For P{i+1}: "))
    arr.append(g)
t=int(input("Enter Time Slice: "))
Process(n,arr,t)
