def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
s=c=0
for i in range(n):
    if prime(l[i])==True:
        s+=l[i]
        c+=1
avg=s/c
print('{:.2f}'.format(avg))