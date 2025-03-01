'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
#1. Companion planting herbs like basil, rosemary, and mint alongside vegetables helps naturally repel pests, keeping your garden healthy and thriving!
#2.Indian Runner Ducks make great natural pest control for gardens, as they eagerly eat slugs, insects, and weeds while roaming without trampling plants while looking cute!
#3. Instead of grass, plant purple creeping thyme to create a fragrant, low-maintenance ground cover that releases a lemony scent and naturally repels insects. Around the areas that aren't used for gardening!

with open("gardening_tips.txt", "r") as file:
    for line in file:
        print(line.strip())

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
#Lion Pass 5
#Snoqualmie Trail 3

file = open("hiking_log.txt", "a")

while True:
    hike_name = input("Enter the hike name (or press 0 to exit): ")
    if hike_name == "0":
        break
    distance = input("Enter the distance in miles: ")
    if distance == "0":
        break
    file.write(hike_name + "\t" + distance + "\n")

file.close()

with open("hiking_log.txt", "r") as file:
    print("\nHiking Log:")
    print(file.read())

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
#I can't be your love
#Cause I'm afraid I'll ruin your life, hmm
#While the leaves withered away
#And grew again
#You have gone far away
#I'll be pushing up daisies
#And bring all the chances to here
#But I'll pray for you all the time
#If I could be by your side
#I'll give you all my life, my seasons
#By your side, I'll be your seasons, hmm
#My love

with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()

# Gets 5 words from the user
word_counts = {}
for i in range(5):
    word = input(f"Enter word {i+1} to count: ").lower()
    word_counts[word] = lyrics.count(word)
print("\nWord Frequency Count:")
print(word_counts)

'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
# Open poll.txt in read mode
'''
#yea,yea,nay,yea,nay,yea,yea,nay,yea,nay,yea,yea,yea,nay,nay
with open("poll.txt", "r") as file:
    votes = file.read().strip().split(",")

yea_count = votes.count("yea")
nay_count = votes.count("nay")

print(f"Yea votes: {yea_count}")
print(f"Nay votes: {nay_count}")


