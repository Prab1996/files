ft = input('do you work fulltime?: ')
try:
    if ft == 'yes':
        x = 40
    if ft == 'no':
        x = input('how many hours you work per week?: ')
    y = input('pay rate per hour?: ')
    pay = int(x) * int(y)
    print('your pay per week is $',pay)
    print('your pay biweekly is $',pay*2)
    print('your pay per year is $',pay*52)
except:
    print('please answer yes or no')
