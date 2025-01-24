# Module 3: Practice Problems

 # 1. Prompt the user for a word. Then, prompt the user for how many times
# they'd like that word repeated. Use the skills you learned in this module to print the
#word the correct number of times.

# User inputs a word
word = input("Enter a word: ")

# User inputs the amount of times theyd like the word repeated
repetition = int(input("How many times would you like the word repeated?: "))

# print the word
print(word * repetition)

 #2. Prompt the user for their name and their age. Calculate their age next year.
#Use string concatenation to print "Hello, <name>! You are <age1> years old.
#Next year, you will be <age2> years old."

# Ask user for name
name = input("Enter your name: ")

# Ask user for age
age = int(input("Enter you age: "))

# Add 1 to there current age
age_next_year = age + 1

# using concantenation to create a message
message = "Hello, " + name +"! You are " + str(age) + " years old! Next year, you will turn "  + str(age_next_year) + " years old!"

print(message)

 #3. Prompt the user for a sentence and a word to try to find in that sentence.
#Have the program print out whether the word was found in the sentence. (i.e. True or False)

# Ask user for a sentence
sentence = input("Please enter a sentence: ")

# Ask the user for a word to find
word = input("Enter a word to find in the sentence: ")

# A variable if word is found
words = sentence.split(" ")

# Checking if the word exists using in
found = word in sentence
print(found)

 #4. Prompt the user for: a word, a first index, and a last index.
#Slice the word at the indexes provided by the user and print to the screen.

# Ask user for word
word = input("Please enter a word: ")

# Ask user for the first index
first_index = int(input("Please enter the first index: "))

# Ask user the the last index
last_index = int(input("Please enter the last index: "))

# Slice the word at the users discretion
sliced_word = word[first_index:last_index]

print("The sliced word is: ", sliced_word)

 #5. Print 3 words with a | character (called a pipe) in between them.
#Use the appropriate keyword argument in print() to do so.

print("apple", "banana", "cherry", sep="|")
