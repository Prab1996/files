def find(y,z):
    count = 0
    z = float(z)
    print(type(y))
    print(type(z))
    for x in y:
        print(type(x))
        x = float(x)
        if x == z:
            count = count + 1
    return count

userlist = input("please enter your list of numbers seprated by space:" )
print(type(userlist))
userlist = userlist.split()
print(type(userlist))
usernumber = input("please enter the number you want to find:" )
result = find(userlist,usernumber)
print(usernumber, "appeared", result, "times in the list")
