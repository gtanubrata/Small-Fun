age = int(input("your age: "))
# 2-8 2 dollar ticket
# 65 5 dollar ticket
# 10 dollar for everyone else

if not ((age >=2 and age <=8) or age >= 65):
    print("YOU PAY 10 DOLLARS and are not a child or senior citizen")
else:
    print("YOU ARE A CHILD OR SENIOR CITIZEN!")
