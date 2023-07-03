n=int(input())
t=n
s=0
if n<0:
    n=-n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if t<0:
    print(-s)
else:
    print(s)