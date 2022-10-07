a,b,c=map(int,input().split())
p=1
for i in range (b):
    p*=a
print(p%c)