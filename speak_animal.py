# Define speak below:
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    if animal == "duck":
        return "quack"
    if animal == "cat":
        return "meow"
    if animal == "dog":
        return "woof"
    return "?"

# More compact solution:
# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"