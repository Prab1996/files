x = input("how many hours did you work last week?")
y = input ("how much is your payrate per hour?")
try:
    x = int(x)
    y = int(y)
    if x > 40:
        ox = x - 40
        rx = x - ox
        oy = (y/2)+y
        ot = ox*oy
        print("your overtime pay is $", ot)
        print("your regular pay is $", rx*y)
        print("your total pay is $", (ot)+(rx*y))
    else:
        print("your total pay is $", (x*y))

except:
    print("please enter hours and payrate as number greater than 0")
