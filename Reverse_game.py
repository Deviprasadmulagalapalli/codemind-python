def rev(n):
    n=str(n)
    s=n[::-1]
    return int(s)
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    print(rev(l[i]),end=' ')