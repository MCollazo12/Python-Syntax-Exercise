# Print out each word on a separate line in all uppercase
def print_upper_words(words):
    for word in words:
        print(word.upper())

# Only print words that start with the letter 'e' (either upper or lowercase)
def print_upper_words2(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())
            
# Takes in a set of letters and only prints words that start with those letters
def print_upper_words3 (words, must_start_with):
    for word in words:
        starting_letter = word[0]
        if starting_letter in must_start_with:
            print(word.upper())