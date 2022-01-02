def find(y,z):
    count = 0
    y = y.split()
    z = float(z)
    for x in y:
        x = float(x)
        if x == z:
            count = count + 1
    return count

userlist = input("please enter your list of numbers seprated by space:" )
usernumber = input("please enter the number you want to find:" )
result = find(userlist,usernumber)
if result > 1:
    print(usernumber, "appeared", result, "times in the list")
elif result == 1:
    print(usernumber, "appeared once on the list")
else:
    print(usernumber, "did not appear on the list")
