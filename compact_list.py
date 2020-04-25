'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(x):
    return [i for i in x if i]



# # COLT'S CODE ------------------------------------------------------------------------
# # elegant

# def compact(l):
#     return [val for val in l if val]

# # without list comprehension
# def compact(l):
#     truthy_vals = []
#     for val in l:
#         if val: truthy_vals.append(val)
#     return truthy_vals

print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]