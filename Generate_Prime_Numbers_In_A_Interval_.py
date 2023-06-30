def prime(n):
    is_prime=True
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
    return is_prime
    
    
n=int(input())
m=int(input())
for j in range(n,m+1):
    if prime(j)==True:
        print(j)