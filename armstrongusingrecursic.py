def is_as(n, b, re=0):
    if n == 0:
        return re
    d = n % 10
    re += d**b
    return is_as(n // 10, b, re)

a = int(input("Enter a number: "))
b = len(str(a)) 
if a == is_as(a, b): 
    print("is armstrong")
else:
    print("not armstrong")