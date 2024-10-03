#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num > second_num and third_num:
    print (f"{first_num} is the biggest number")

elif second_num > third_num and first_num:
    print (f"{second_num} is the biggest number")
        
else:
    print(f"{third_num} is the biggest number")