# Check Even or Odd

num = input("Enter any number: ");
if num == 'x':
    exit();
try:
    number = float(num);
except ValueError:
    print("Please, enter a number...");
else:
    check = number % 2;
    if check == 0:
        print(int(number), "is an even number.");
    elif check == 1:
        print(int(number), "is an odd number.");
    else:
        print(number, "is strange.");
