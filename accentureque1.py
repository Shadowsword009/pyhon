def minstep(n, count=0):
    if n == 1:
        return count
    if n % 2 == 0:
        return minstep(n // 2, count + 1)
    else:
        return minstep(n + 1, count + 1)

x = int(input("Enter a number: "))
print(minstep(x))
