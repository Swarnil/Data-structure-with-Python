count = 1
n = input("ENTER THE binary number series: ")
print(n[0],end='')
for i in range(1,len(n)):
    if n[i+1]==n[i]:
        count+=1

print(count)
