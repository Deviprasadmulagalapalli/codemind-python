n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
a=list(a)
b=set(b)
b=list(b)
c=0
for i in range(len(a)):
    if a[i] not in b:
        c+=1
for i in range(len(b)):
    if b[i] not in a:
        c+=1
print(c)