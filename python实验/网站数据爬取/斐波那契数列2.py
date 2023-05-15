def fib_yield_while(max):
    a,b = 0,1
    while max > 0 :
        a,b = b,a + b
        max -= 1
        yield a

def fib_yield_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

num = int(input("输入所求数列的个数:"))

print(0,end = " ")
#for i in fib_yield_while(num-1):
#    print(i,end=" ")

for Fibo in fib_yield_for(num-1):
        print(Fibo,end=" ")