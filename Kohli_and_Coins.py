n=int(input())
if n%10==0:
    print(n//10)
elif n%5==0:
    print((n//10)+1)
else:
    print(-1)