print("Enter marks obtained in 5 subjects: ");
m1 = input();
m2 = input();
m3 = input();
m4 = input();
m5 = input();

mark1 = int(m1);
mark2 = int(m2);
mark3 = int(m3);
mark4 = int(m4);
mark5 = int(m5);

sum = mark1 + mark2 + mark3 + mark4 + mark5;

average = sum/5;
percentage = (sum/500)*100;
print("out of 500 ",sum);
print("Average Marks = ", average);
print("Percentage Marks = ", percentage,"%");