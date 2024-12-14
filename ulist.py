l = list(map(int, input().split()))
l1 = []
l2 = []
for i in l:
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)
l2.sort()
l1.sort()
print(l1[::-1] + l2)