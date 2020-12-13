i=int(input("You want to find the fibonacci sequence till->"))
#Finding Fibonacci sequence till given input

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b

fib(i)
input("\nPress Enter to Exit")