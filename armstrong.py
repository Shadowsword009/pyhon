a = int(input("Enter a number: "))
b = len(str(a))
if a == sum(int(digit) ** b for digit in str(a)):
    print("it is an Armstrong number.")
else:
    print("it is not an Armstrong number.")
