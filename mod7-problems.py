'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for character in word if character in vowels)

words = ["Kuromi", "My Melody", "Panpanpurin", "Hello Kitty"]
for word in words:
    print(f"count_vowels('{word}') = {count_vowels(word)}")


'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''

def is_palindrome(s):
    cleaned_s = s.lower().replace(" ", "")  # Convert to lowercase & remove spaces
    return cleaned_s == cleaned_s[::-1]

phrases = ["peep", "mochi", "taco cat", "Soup"]
for phrase in phrases:
    print(f"is_palindrome('{phrase}') = {is_palindrome(phrase)}")

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
    effectiveness = {
        ("Water", "Fire"): "Super Effective",
        ("Fire", "Water"): "Not Very Effective",
        ("Electric", "Grass"): "Neutral",
    }
    return effectiveness.get((attacker, defender), "Neutral")

battles = [("Fire", "Water"), ("Water", "Fire"), ("Electric", "Grass")]
for attacker, defender in battles:
    print(f"type_advantage('{attacker}', '{defender}') = {type_advantage(attacker, defender)}")


'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if age <= 18: return 0
    if age >= 65: return 15 if vehicle else 5
    return 20 if vehicle else 10

passengers = [(15, True), (30, False), (70, True), (45, True), (18, False)]
for age, vehicle in passengers:
    print(f"ferry_fare({age}, {vehicle}) = ${ferry_fare(age, vehicle)}")

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
# Function to determine player level based on experience points
def level_up(experience):
    if experience >= 200:
        return 3
    if experience >= 100:
        return 2
    return 1

experiences = [50, 150, 250, 99, 100, 199, 200]
for xp in experiences:
    print(f"level_up({xp}) = Level {level_up(xp)}")
