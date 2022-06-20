vowels="aeiou"
str = input("Enter the string: ")
str = str.casefold()
count={}.fromkeys(vowels,0)

for char in str:
    if char in count:
        count[char]+=1
print(count)
