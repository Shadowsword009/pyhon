a = int(input("Enter a number: "))
b = len(str(a))
n = sum(int(digit) for digit in str(a))
print(n)
count = 0
for i in range (2,n):
    if n % i == 0:
        count += 1
if count == 0:
    print("prime")
else:
    print("not prime")