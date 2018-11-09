
# Swap Two Numbers

num1 = input("Enter first number: ");
num2 = input("Enter second number: ");

print("\nStarted swapping the given two numbers...");
number1 = int(num1);
number2 = int(num2);

print("Value of First and Second number BEFORE swapping:");
print("First Number =",number1,"\nSecond Number=",number2);

swap = number1;
number1 = number2;
number2 = swap;

print("Value of First and Second number AFTER swapping:");
print("First Number =",number1,"\nSecond Number=",number2);