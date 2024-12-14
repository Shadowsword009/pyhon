def sum_of_digits(n, re=0):
    if n == 0:
        return re
    d = n % 10 
    re = re + d    
    return sum_of_digits(n // 10, re)

a = int(input("Enter a number: "))
print(sum_of_digits(a))