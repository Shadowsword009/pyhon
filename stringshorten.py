s = input()
stack= []
a = len(s)
for i in range(len(s)):
    if stack == s[i]==stack[1]:
        stack.pop()
    else:
        stack.append(s[i])
print("".join(stack)) 