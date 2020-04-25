'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

# def frequency(values, val):
#     count = 0
#     for i in values:
#         if val == i:
#             count += 1
#     return count



# COLT'S CODE --------------------------------------------------

def frequency(collection, searchTerm):
    return collection.count(searchTerm)

print(frequency([1,2,3,4,4,4], 4)) # 3
print(frequency([True, False, True, True], False)) # 1