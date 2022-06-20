str= input("ENTER THE TEXT: ")
print(str[0],end='')
for i in range(1,len(str)):
    if str[i-1]==str[i]:
        print("*",end='')
    else:
        print(str[i],end='')
