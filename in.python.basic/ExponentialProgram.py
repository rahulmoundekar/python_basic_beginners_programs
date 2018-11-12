num=int(input("enter any number you want to : "))
exp=int(input("enter exponential number: "))
result=1
for i in range(1,(exp+1)):
    result=result*num
print("The result is : ",result)