c,d,a,b=map(int,input().split())
n=abs(c-d)
if a<=b:
    s=a*c
    print(s)
else:
    s=(a*d)+(b*n)
    print(s)