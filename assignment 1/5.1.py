list=[]
print("enter five numbers")
for i in range(0,5):
    num=int(input("enter number"))
    list.append(num)
print(list)
largest=max(list)
smallest=min(list)
print("largest number is ",largest)
print("smallest number is ",smallest)