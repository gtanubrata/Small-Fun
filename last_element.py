'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(x):
    if len(x) > 1:
        return x[-1]
    None


# ELEGANT SOLUTION -----------------------------------------------

# First check to see if the list exists (if it has data in it).
# If it does, return the -1 item (last item).
# Otherwise, return None.

# def last_element(l):
#     if l:
#         return l[-1]
#     return None