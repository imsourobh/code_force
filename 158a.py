ans= False
while(ans==True):
    n, k=map(int,input().split())
    if n>k:
        ans=True
count=0
num=list(map(int,input().split()))
for i in num:
    if i> num[k-1]:
        count=count+1

print(count)