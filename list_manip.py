'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(x, command, loc, val=None):
    if command == "remove" and loc == "end":
        return x.pop()
    elif command == "remove" and loc == "beginning":
        return x.pop(0)
    elif command == "add" and loc == "beginning":
        x.insert(0, val)
        return x
    elif command == "add" and loc == "end":
        x.append(val)
        return x
    else:
        return "invalid input"

print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]