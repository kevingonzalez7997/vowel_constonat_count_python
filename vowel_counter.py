def vowel_counter(word):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    consonant_count = 0 
    for letter in word:
        if letter.lower() in vowels:
            vowel_count += 1
        elif letter.isalpha():
            consonant_count += 1
    print(f"The number of v is {vowel_count}")
    print(f"The number of constonat is {consonant_count}")
vowel_counter("Hello World")
