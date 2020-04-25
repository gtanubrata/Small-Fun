# ask for age
# 18-21 wristband
# 21+ drink, normal entry
# too young, sorry

# age = input("how old are you? ")
# if age:
#     age = int(age)
#     if age >=18 and age < 21:
#         print("you can enter, but need a wristband")
#     elif age >= 21:
#         print("you are good to enter and can drink")
#     else:
#         print("you can't come in, little one :(")
# else:
#     print("please enter your age.")

age = input("how old are you? ")
if age:
    age = int(age)
    if age >= 21:
        print("you are good to enter and can drink")
    elif age >= 18:
        print("you can enter, but need a wristband")
    else:
        print("you can't come in, little one :(")
else:
    print("please enter your age.")
