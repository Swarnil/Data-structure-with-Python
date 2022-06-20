arr = [20, 15, 18, 60, 30, 45, 36]
l = 0
h = len(arr)-1

# Merge Function
def Merge (arr,l,m,h):
    i = l
    j = m+1
    c = []

    while(i<=m and j<=h):
        if arr[i] <= arr[j]:
            c.append(arr[i])
            i+=1
        else:
            c.append(arr[j])
            j+=1
    
    while(i<=m):
        c.append(arr[i])
        i+=1
    
    while(j<=h):
        c.append(arr[j])
        j+=1
    
    i=l
    k=0
    while i<=h:
        arr[i] = c[k]
        i+=1
        k+=1

# MergeShort function
def MergeSort(arr,l,h):
    if l<h:
        m = (l+h)//2
        MergeSort(arr,l,m)
        MergeSort(arr,m+1,h)
        Merge(arr,l,m,h)

# Function Call
MergeSort(arr,l,h)
print(arr)