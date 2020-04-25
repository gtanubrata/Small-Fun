'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
# def multiple_letter_count(string):
#     count = []
#     for i in range(len(string)):
#         count.append(string.count(string[i]))
#     return { key:val for key, val in zip(string, count) }

# print(multiple_letter_count("awesome")) # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

# COLT'S CODE ------------------------------------------------------------------------------

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

print(multiple_letter_count("awesome")) # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}