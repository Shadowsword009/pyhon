def fun(x,y):
    if x == 0:
        return 0
    print(y,end="\t")
    fun(x-1,y+1)
    if y!=0:
        print(y,end="\t")
def fun2(n,m):
    if n==0:
        return 0
    print(m)
    fun(n-1,m+1)
    if (m-1)!=0:
        print(m-1)

x,y = 5,1
fun(x,y)
fun2(x,y)