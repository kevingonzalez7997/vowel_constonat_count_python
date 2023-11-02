def vowel_counter(word):
    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # Iterate through each character in the word
    for letter in word:
        # Check if the lowercase of the letter is in the list of vowels
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            # If it's a vowel, increment the vowel count
            vowel_count += 1
        # Check if the character is an alphabet character (not a symbol or space)
        elif letter.isalpha():
            # If it's a consonant, increment the consonant count
            consonant_count += 1

    # Print the counts of vowels and consonants
    print(f"The number of vowels is {vowel_count}")
    print(f"The number of consonants is {consonant_count}")
