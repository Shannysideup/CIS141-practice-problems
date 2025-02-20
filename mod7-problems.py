'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(input):
    count = 0  # Counts from zero
    for character in input:
        if character in "aeiouAEIOU":  # Checks if its a vowel (both lowercase & uppercase)
            count += 1  # Increase count
    return count  # Return the total number of vowels


print(count_vowels("Kuromi"))  # Output: 3
print(count_vowels("My Melody"))  # Output: 2
print(count_vowels("Panpanpurin"))  # Output: 4
print(count_vowels("Hello Kitty"))  # Output: 3

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palindrome(s):
    s = s.lower()  # switches to lowercase to ignore
    s = s.replace(" ", "")  # gets rid of spaces to handle multi-word palindromes
    return s == s[::-1]  # Compare original with reversed

print(is_palindrome("peep"))  # Output: True
print(is_palindrome("mochi"))  # Output: False
print(is_palindrome("taco cat"))  # Output: True
print(is_palindrome("Soup"))  # Output: False


'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
def type_advantage(attacker, defender):
    if attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
    else:
        return "Neutral"


print(type_advantage("Fire", "Water"))  # Output: Not Very Effective
print(type_advantage("Water", "Fire"))  # Output: Super Effective
print(type_advantage("Electric", "Grass"))  # Output: Neutral


'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    if age <= 18:  # Children (0-18)
        return 0
    elif age >= 65:  # Seniors (65+)
        if vehicle:
            return 15
        else:
            return 5
    else:  # Adults (19-64)
        if vehicle:
            return 20
        else:
            return 10

print(ferry_fare(15, True))  # Output: 0 (Kids ride free)
print(ferry_fare(30, False))  # Output: 10 (Adult without vehicle)
print(ferry_fare(70, True))  # Output: 15 (Senior with vehicle)
print(ferry_fare(45, True))  # Output: 20 (Adult with vehicle)
print(ferry_fare(18, False))  # Output: 0 (Kid)
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
def level_up(experience):
    if experience >= 200:
        return 3  # Level 3
    elif experience >= 100:
        return 2  # Level 2
    else:
        return 1  # Level 1


print(level_up(50))   # Output: 1 (0-99 XP → Level 1)
print(level_up(150))  # Output: 2 (100-199 XP → Level 2)
print(level_up(250))  # Output: 3 (200+ XP → Level 3)
print(level_up(99))   # Output: 1 (Still Level 1)
print(level_up(100))  # Output: 2 (Exact 100 XP → Level 2)
print(level_up(199))  # Output: 2 (Still Level 2)
print(level_up(200))  # Output: 3 (Exact 200 XP → Level 3)
