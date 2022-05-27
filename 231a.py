n=int(input())
count=0
for i in range(n):
    x,y,z=input().split()
    if int(x)==1 and int(y)==1 or int(x)==1 and int(z)==1 or int(z)==1 and int(y)==1 or int(x)==1 and int(y)==1 and int(z)==1:
        count=count+1
    else:
        pass

print(count)