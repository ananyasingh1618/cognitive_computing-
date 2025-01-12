string="hello today is sunday"
count=0
for i in string:
    if i in "aeiouAEIOU":
        count=count+1
print(count)