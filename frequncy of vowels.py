data = str(input("Enter the sentence: "))
vowels= "aeiouAEIOU"
for v in vowels:
    print(v,data.lower().count(v))
