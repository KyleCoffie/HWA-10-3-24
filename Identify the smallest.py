#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num < second_num and third_num:
    print("The smallest number is:"+ first_num)
    
elif second_num < third_num and first_num:
    print("The smallest number is:"+ second_num)
    
else:
    print("The smallest number is: "+ third_num)