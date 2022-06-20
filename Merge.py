class MergeSort:
    def Merge(self,arr,l,m,h):
        i=l
        j=m+1
        c=[]
        while i<=m and j<=h:
            if arr[i]<=arr[j]:
                c.append(arr[i])
                i+=1
            else:
                c.append(arr[j])
                j+=1
        while i<=m:
            c.append(arr[i])
            i+=1
        while j<=h:
            c.append(arr[j])
            j+=1
        i=l
        k=0
        while i<=h:
            arr[i]=c[k]
            i+=1
            k+=1
    def MergeSort(self,arr,l,h):
        if l<h:
            m=(l+h)//2
            ob.MergeSort(arr,l,m)
            ob.MergeSort(arr,m+1,h)
            ob.Merge(arr,l,m,h)
if __name__=='__main__':
    ob=MergeSort()
    arr=[5,7,10,2,30,0,8,50]
    l=0
    h=len(arr)-1
    ob.MergeSort(arr,l,h)
    print(arr)

