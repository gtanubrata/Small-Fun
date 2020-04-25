'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

# def number_compare(x,y):
#     if x == y:
#         return "Numbers are equal"
#     elif x > y:
#         return "First is greater"
#     elif x < y:
#         return "Second is greater"
#     None

# COLT'S CODE ---------------------------------

def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"