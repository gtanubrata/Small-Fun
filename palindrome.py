'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(word):
    stripped = (word.replace(" ", "")).lower()
    # print(stripped)
    if stripped == stripped[::-1]:
        return True
    return False


# COLT'S CODE --------------------------------------------------

# def is_palindrome(string):
#     stripped = string.replace(" ", "")
#     return stripped == stripped[::-1]

print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('a man a plan a canal Panama')) # True
print(is_palindrome('Mr Owl ate my metal worm')) # True