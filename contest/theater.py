n,m,a =map(int,input().split())

if n%a==0:
    n=(n//a)
else:
    n=(n//a)+1

if m%a!=0:
    m=(m//a)+1
else:
    m=m//a

print(m*n)