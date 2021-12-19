salary = input('how much is your salary?: ')
try:
    salary = int(salary)
except:
    salary = -1
if salary > 0:
    print('your pay per hour is is $',(salary/52)/40)
    print('your pay per week is $',salary/52)
    print('your pay biweekly is $',salary/26)
    print('your pay per month is $',salary/12)
    if salary > 30000:
        if salary <=60000:
            print('you are doing great')
    if salary > 60000:
        if salary <=90000:
            print('you are in the top 20% middle class')
    if salary > 90000 :
        if salary <= 1000000 :
            print('you are in top 1% of usa population')
    if salary > 1000000 :
        print('you are in top 0.01% of usa population')
else:
    print('salary need to be a number more than 0')
