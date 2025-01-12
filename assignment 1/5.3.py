list=[]
print("Enter 5 numbers")
for i in range(0,5):
    num=int(input("Enter number"))
    list.append(num)
print(list)
ascending=sorted(list)
descending=sorted(list,reverse=True)
print("Ascending order is ",ascending)
print("Descending order is ",descending) 