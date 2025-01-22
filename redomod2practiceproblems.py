# Resubmission of module 2 practice problems

# 1. Create a program that prints the following output to the screen:
#"Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony.
#Then, everything changed when the Fire Nation attacked."

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony.")

# 2. Create a program that prompts for 2 numbers and then outputs the
#addition, subtraction, multiplication, and division of the first number by the second number.

#input for two numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

#Perform calculations with comments
print("Addition:", num1 + num2) #Addition
print("Subtraction:", num1 - num2) #Subraction
print("Multiplication:", num1 * num2)#Multiplication
print ("Division:", num1 / num2) # Division

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula.
#(https://en.wikipedia.org/wiki/Heron%27s_formula)
#In geometry, Heron's formula (or Hero's formula) gives the area of a triangle in terms of the three side lengths ⁠
#a,b,c. Letting s be the semiperimeter of the triangle s=1/2(a+b+c), the area A is
#A = Sqrt s(s-a)(s-b)s-c)

# Prompt for the side lengths of the triangle
A = float(input("Enter the length of the first side: "))
B = float(input("Enter the length of the second side: "))
C = float(input("Enter the length of the third side: "))

# Triangle lengths
a = float(input)("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

#Calculate the semiperimeter
s = (a+b+c) / 2

#area using Herons Forumlua
area = (s * (s - a) * (s - b) * (s - c)) **0.5
print ("The area of the triangle is:", area)

#4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation

# Input five numbers
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
n4 = float(input("Enter the fourth number: "))
n5 = float(input("Enter the fifth number: "))

#compute total
total = n1 + n2 + n3 + n4 + n5
print("Total:", total)  #total

# compute average
average = total / 5
print("Average:", average)  # average

# Compute minimum and maximum
minimum = min(n1, n2, n3, n4, n5)
maximum = max(n1, n2, n3, n4, n5)
print("Minimum:", minimum)  # Output minimum
print("Maximum:", maximum)  # Output maximum

# Compute range
range_value = maximum - minimum
print("Range:", range_value)  #range

# Compute standard deviation
difference1 = (n1 - average) ** 2
difference2 = (n2 - average) ** 2
difference3 = (n3 - average) ** 2
difference4 = (n4 - average) ** 2
difference5 = (n5 - average) ** 2
variance = (difference1 + difference2 + difference3 + difference4 + difference5) / 5
std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)  #standard deviation

