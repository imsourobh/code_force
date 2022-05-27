#boy or girl

name=input()
name_list=''
for i in name:
    if i not in name_list:
        name_list=name_list+i
if len(name_list)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
