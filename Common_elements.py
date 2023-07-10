n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
a1=[]
b1=[]
for i in range(len(a)):
    if a[i] not in a1:
        a1.append(a[i])
for i in range(len(b)):
    if b[i] not in b1:
        b1.append(b[i])
for i in range(len(a1)):
    if a1[i] in b1:
        l.append(a1[i])
for i in range(len(l)):
    print(l[i],end=' ')