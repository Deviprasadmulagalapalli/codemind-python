n=int(input())
m=int(input())
for i in range(n,m+1):
    t=i
    l=str(t)
    c=0
    while i!=0:
        r=i%10
        if r==0:
            pass
        elif t%r==0:
            c+=1
        i=i//10
    if c==len(l):
        print(t,end=' ')