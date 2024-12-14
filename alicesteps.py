n = int(input("no of steps:"))
m = int(input("max steps alice can take:"))
result = n/m
if (n%m==0):
    print(result)
else:
    print(result//m+1)