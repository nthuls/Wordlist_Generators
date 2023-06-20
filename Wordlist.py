import datetime
import itertools

# Function to generate the wordlist
def generate_wordlist(length):
    wordlist = []
    for i in range(length):
        word = input("Enter character #{}: ".format(i + 1))
        wordlist.append(word.lower())  # Store lowercase version
        wordlist.append(word.upper())  # Store uppercase version
    return wordlist


# Ask user for the desired length of the wordlist
length = int(input("Enter the length of the wordlist: "))

# Generate the wordlist
wordlist = generate_wordlist(length)

# Ask user if they want to save the wordlist
save_option = input("Do you want to save the output in a text file? (y/n): ")

# If user wants to save the wordlist
if save_option.lower() == 'y' or save_option.lower() == 'yes':
    # Ask for filename
    filename = input("Enter the filename for the wordlist (without extension): ")

    # Generate a unique filename using the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_with_time = "{}_{}.txt".format(filename, current_time)

    # Save the wordlist to the file
    with open(filename_with_time, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

    print("Wordlist saved as {}".format(filename_with_time))
    print()
else:
    # Print the wordlist
    print("Wordlist:")
    for word in wordlist:
        print(word)
    print()

# Generate all possible combinations
combinations = list(itertools.permutations(wordlist))

# Append the combinations to the existing file
with open(filename_with_time, 'a') as file:
    file.write("\nCombinations:\n")
    for combo in combinations:
        file.write(''.join(combo) + '\n')

print("Combinations saved to {}".format(filename_with_time))
