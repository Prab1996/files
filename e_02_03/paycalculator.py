ft = input('do you work fulltime?: ')
try:
    if ft == 'yes':
        x = 40
    if ft == 'no':
        x = input('how many hours you work per week?: ')
    try:
        x = float(x)
        x > 0
        y = input('pay rate per hour?: ')
        try:
            y = float(y)
            if y > 0:
                pay = int(x) * int(y)
                print('your pay per week is $',pay)
                print('your pay biweekly is $',pay*2)
                print('your pay per year is $',pay*52)
            else:
                print('payrate should be higher than 0, if it is not please call 911')
        except:
            print('please enter a number')
    except:
        print('enter your hours in a number higher than 0')
except:
    print('please answer yes or no')
