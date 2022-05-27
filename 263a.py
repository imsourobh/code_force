count=0
for i in range(5):
    line=list(map(int, input().split()))
    for j in range(5):
        if str(line[j])=='1':
            count=1
            break
            
    if count==1:
        break
i=i+1
j=j+1
if i >3:
    i=i-3
else:
    i=3-i
if j>3:
    j=j-3
else:
    j=3-j
print(i+j)