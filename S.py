# a=[1,2,3]
# for i in a:
#     for j in a:
#         print(i+j)

def suvanker(a,l,i,j):
    if i==l:
        return    
    print(a[i]+a[j])
    j+=1
    if j!=l:
        suvanker(a,l,i,j)
    if j==l:
        i+=1
        j=0
        suvanker(a,l,i,j)
a=[1,2,3]
l=len(a)
i=0
j=0
suvanker(a,l,i,j)
