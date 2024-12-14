def count_odd_digits(number):
    number_str = str(number)
    odd_digits_count = 0
    
    for digit in number_str:
        
        if int(digit) % 2 != 0:
            odd_digits_count += 1
            
    return odd_digits_count


