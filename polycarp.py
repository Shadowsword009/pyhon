n = int(input("Enter the number of test cases: "))
for _ in range(n):
    k = int(input("Enter the value of k: "))
    i = 1
    count = 0
    while True:
        if i % 3 != 0 and i % 10 != 3:
            count += 1
            if count == k:
                print(i)
                break
        i += 1
