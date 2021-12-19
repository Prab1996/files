ft = input('do you work fulltime?: ')
if ft == 'yes':
    x = 40
if ft == 'no':
    x = input('how many hours you work per week?: ')
y = input('pay rate per hour?: ')
pay = int(x) * int(y)
print('your pay per week is $',pay)
print('your pay biweekly is $',pay*2)
print('your pay per year is $',pay*52)

salary = input('how much is your salary?: ')
print('your pay per hour is is $',(int(salary)/52)/40)
print('your pay per week is $',int(salary)/52)
print('your pay biweekly is $',int(salary)/26)
print('your pay per month is $',int(salary)/12)
