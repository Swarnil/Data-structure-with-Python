n=input("Enter Digit:(2-4):")
l=[]
a=[['a','b','c'],
['d','e','f'],
['g','h','i'],
['j','k','l'],
['m','n','o'],
['p','q','r','s'],
['t','u','v'],
['w','x','y','z']]
for i in range(len(n)):
    if n[i]=="2":
        l.append(a[0])
    elif n[i]=="3":
        l.append(a[1])
    elif n[i]=="4":
        l.append(a[2])
    elif n[i]=="5":
        l.append(a[3])
    elif n[i]=="6":
        l.append(a[4])
    if n[i]=="7":
        l.append(a[5])
    elif n[i]=="8":
        l.append(a[6])
    elif n[i]=="9":
        l.append(a[7])
new_list=[]
if len(l)==0:
    print(l)
elif len(l)==1:
    print(l[0])
else:
    for i in range(len(l[0])):
        for j in range(len(l[1])):
            new_list.append(l[0][i]+l[1][j])
    print(new_list)
