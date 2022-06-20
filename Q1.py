class Solution:
    def __init__(self):
        pass

    def isValid(self, s):
        f = 0
        st = []

        for i in s:
            if i in ['(', '{', '[']:
                st.append(i)
            if i in [')', '}', ']']:
                if i == '}':
                    if '{' in st:
                        st.remove('{')
                if i == ']':
                    if '[' in st:
                        st.remove('[')
                if i == ')':
                    if '(' in st:
                        st.remove('(')
        # print(st)
        if len(st) == 0:
            print("true")
        else:
            print("false")
obj = Solution()
s = input()
f = 0

for i in s:
    if i not in ['(', '{', '[', ')', '}', ']']:
        f = 1
if len(s)>=1 and len(s)<=1000 and f==0:
    obj.isValid(s)
else:
    print("Invalid")
