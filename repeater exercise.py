n = int(input("How many times do I have to tell you? "))

for time in range(n):
    print(f"Time {time+1}: CLEAN UP YOUR ROOM!")
    if time >= 3:
        print("Do you even listen anymore?")
        break