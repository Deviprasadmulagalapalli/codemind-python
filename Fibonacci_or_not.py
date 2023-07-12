def fib(n):
    a=0
    b=1
    while b<n:
        sum=a+b
        a=b
        b=sum
    if a==n or b==n:
        return True
    else:
        return False
n=int(input())
print(fib(n))