MAX = 100000
 
def Print3rdSmallest(arr, n):
    min1 = MAX
    min2 = MAX
    min3 = MAX
    
    for i in range(0, n):
        if arr[i] < min1:
            min3 = min2
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min3 = min2
            min2 = arr[i]
        elif arr[i] < min3:
            min3 = arr[i]
 
    print("Third min = ", min3)
 
arr = eval(input("Enter the elements: "))
n = len(arr)
Print3rdSmallest(arr, n)