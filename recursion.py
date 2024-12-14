def fun(a):
    if a >= 0:
        b = a
        print(b, end='\t')
        fun(a-1)
        if a > 0:
            c = a
            print(c, end='\t')

def fun2(a):
    if a >= 0:
        b = a
        print(b, end='\t')
        if a > 1:  
            fun2(a-2)
        if a > 1:
            c = a
            print(c, end='\t')

x = int(input())
fun(x)
print()
fun2(x)

