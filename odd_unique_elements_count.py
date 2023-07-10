n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
c=0
for i in range(len(l)):
    if l[i]%2!=0:
        c+=1
print(c)