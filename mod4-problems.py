# Mod 4 Practice Problems

#1. Construct a truth table for the expression:
#(A AND B) OR (NOT B) where A and B each can be True or False.
#Your truth table should be commented out (as it's not valid Python code!)

# A       B       A AND B   NOT B    (A AND B) OR (NOT B)
# ------------------------------------------------------
# True    True    True      False    True
# True    False   False     True     True
# False   True    False     False    False
# False   False   False     True     True

#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold.
#If a sensor threshold is below the number 8, print "Headlights On";
#otherwise, print "Headlights Off".

sensor_threshold = int(input("Enter the sensor threshold: "))
if sensor_threshold < 8:
    print("Headlights On")
else:
    print("Headlights Off")

#3. Prompt the user for their bank balance.
#Evaluate whether the balance is less than $100.
#Print True if the user’s balance is below $100; print False, otherwise.

balance = float(input("Enter your bank balance: "))
print(balance < 100)

#4. A theater wants to enforce age restrictions for movie tickets.
#Ask the user for their age, and tell them whether they can see G (appropriate for under 13),
#PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.

there_age = int(input("Enter your age: "))

if there_age < 13:
    print("You can watch G rated movies!")
elif 13 <= there_age <= 17:
    print("You can watch PG-13 movies!")
else:
    print("You can watch R rated movies!")

#5. A store charges $5 for shipping on any order under $50.
#If the order amount is $50 or more, shipping is free.
#Ask the user for the order total and print the total cost, including shipping.

order_total = float(input("Enter your order total: "))
if order_total < 50:
    total_cost = order_total + 5
else:
    total_cost = order_total
print("Total cost including shipping:", total_cost)

