'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(nums):
    evens = [n for n in nums if n%2 == 0]
    product = 1
    for i in range(len(evens)):
        product *= evens[i]
    return product

print(multiply_even_numbers([2,3,4,5,6])) # 48



# COLT'S CODE ------------------------------------------

# def multiply_even_numbers(lst):
#     total = 1
#     for val in lst:
#         if val % 2 == 0:
#             total = total * val
#     return total