n=int(input())
l=list(map(int,input().split()))
for i in range(0,n,2):
    t=l[i+1]
    while t>0:
        print(l[i],end=' ')
        t-=1
        