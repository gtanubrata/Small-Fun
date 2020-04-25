'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''
days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
def return_day(num):
    if num in days.keys():
        return days[num]
    None

print(return_day(2))


# # LIST VERSION -----------------------------------------------------------------------------------

# def return_day(num):
#     days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
#     # Check to see if num valid
#     if num > 0 and num <= len(days):
#         # use num - 1 because lists start at 0 
#         return days[num-1]
#     return None

# # ADVANCED VERSION -------------------------------------------------------------------------------

# def return_day(num):
#     try:
#         return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
#     except IndexError as e:
#         return None