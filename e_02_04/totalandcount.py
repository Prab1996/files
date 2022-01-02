tot = 0
count = 0
print('This program will give you a sum, count, and average of numbers you will enter')
print('please enter "done" when you are done and the program will give you result')
x = input('please input your first number:')
x = float(x)
tot = tot + x
count = count + 1
while True :
    y = input('please input your next number:')
    if y == "done":
        break
    try:
        y = float(y)
        tot = tot + y
        count = count + 1
    except:
        print('please enter number')
        continue
print('your total =', tot)
print('count of numbers =', count)
print('avreage of numbers entered =', tot/count)
