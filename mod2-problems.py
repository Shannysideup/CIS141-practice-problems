# Mod 2 practice problems 

# 1. Create a program that prints the following output to the screen: 
#"Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
#Then, everything changed when the Fire Nation attacked."

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony.")

# 2. Create a program that prompts for 2 numbers and then outputs the 
#addition, subtraction, multiplication, and division of the first number by the second number.

#prompt the user for two numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

#Perform calculations with comments 
print(f"{num1} + {num2} = {num1 + num2}") #Addition
print(f"{num1} - {num2} = {num1 - num2}") #Subraction 
print(f"{num1} * {num2} = {num1 * num2}") #Multiplication
print(f"{num1} / {num2} = {num1 / num2}") #Division

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. 
#(https://en.wikipedia.org/wiki/Heron%27s_formula)
#In geometry, Heron's formula (or Hero's formula) gives the area of a triangle in terms of the three side lengths ⁠
#a,b,c. Letting s be the semiperimeter of the triangle s=1/2(a+b+c), the area A is 
#A = Sqrt s(s-a)(s-b)s-c)

# Prompt for the side lengths of the triangle
A = float(input("Enter the length of the first side: "))
B = float(input("Enter the length of the second side: "))
C = float(input("Enter the length of the third side: "))

# Calculate the semi-perimeter
S = (A + B + C) / 2

# Checking the triangle 
if A + B > C and A + C > B and B + C > A: 

# Computing the area using the formula 
 area = (S * (S - A) * (S - B) * (S - C)) ** 0.5 
 print(f"The area of the triangle is: {area:.2f}")
else: 
 print("The entered side lengths do not form a valid triangle.")

# 4. Create a program that computes different statistics given five numbers including the total,
#average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

import math

# Prompt for the five numbers 
numbers = []
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)
    
# Calculate total 
total = sum(numbers) 

# Calculate average 
average = total / len(numbers) 

# Calculate minimum 
minimum = min(numbers) 

# Calculate maximum
maximum = max(numbers) 

# Calculate range
range_value = maximum - minimum 

# Calculate standard deviation 
mean = average 
squared_differences = [(x - mean) ** 2 for x in numbers]
variance = sum(squared_differences) / len(numbers)
std_deviation = math.sqrt(variance)

# Print the results 
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_value}")
print(f"Standard Deviation: {std_deviation:.2f}")
