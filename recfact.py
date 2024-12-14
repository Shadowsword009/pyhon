def fac(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n*fac(n-1)
x = int(input())
print(fac(x))