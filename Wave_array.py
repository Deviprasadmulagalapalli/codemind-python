n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n-1,2):
    if a[i-1]<a[i] and a[i+1]<a[i]:
        c+=1
    elif a[i-1]>a[i] and a[i+1]>a[i]:
        c+=1
    else:
        print('no')
        break
else:
    print('yes')