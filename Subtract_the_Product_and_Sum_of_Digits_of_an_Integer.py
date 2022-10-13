n=int(input())
pd=1
s=0
while n>0:
    r=n%10
    pd*=r
    s+=r
    n=n//10
print(pd-s)