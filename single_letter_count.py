'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
# def single_letter_count(word, letter):
#     word, letter = word.lower(), letter.lower()
#     if letter in word:
#         return word.count(letter)
#     else:
#         return 0

# COLT'S CODE ------------------------------------------

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

print(single_letter_count("Hello World", "h")) # 1
print(single_letter_count("Hello World", "z")) # 0
print(single_letter_count("HelLo World", "l")) # 3