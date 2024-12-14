a = list(input().split())
d = []
for i in a:
    c = a.count(i)
    if c % 2 == 1 and i not in d:
        d.append(i)
print(d)
