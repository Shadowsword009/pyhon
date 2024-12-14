l1 = list(input().split())
l1.sort()
a = 0
t = 0
for i in l1:    
    if t >= 3:
        break
    a = a + int(l1[t])
    t+= 1

print(a)
