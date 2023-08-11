character = input("Enter a character: ")  
  
# Creating a list of vowels  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
if character in vowels:  
    print(f"The character '{character}' is a vowel!")  
else:  
    print(f"The character '{character}' is a consonant!")  

    
#__________________________________________________________________


# sentence = input("Enter a sentence or word: ")

# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# vowel_count = 0
# consonant_count = 0

# for character in sentence:
#     # Check if the character is a vowel
#     if character in vowels:
#         vowel_count += 1
#     else:
#         consonant_count += 1

# print(f"Number of vowels: {vowel_count}")
# print(f"Number of consonants: {consonant_count}")
