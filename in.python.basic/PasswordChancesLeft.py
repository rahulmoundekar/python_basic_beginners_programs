password = "rahul"
for i in range(3):
    pwd=input("Enter Password")
    j=2
    if(pwd==password):
        print("Welcome to Profile")
        break
    else :
        print("Enterd Wrong Password and chances Left : ",j-i);
        continue
print("try next time..visit again..!!!")
