l = list(map(int, input().split()))
l1 = []
a = len(l)
for i in range(a):
    if i % 2 == 0:
        if l[i] % 2 == 1:
            l1.append(i)
print(l1)