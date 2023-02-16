#Alexander Ho
#1677933

current_month = int(input())
current_day = int(input())
current_year = int(input())
birth_month = int(input())
birth_day = int(input())
birth_year = int(input())

print('Birthday Calculator')
print('Current day')
print('Month:', current_month)
print('Day:', current_day)
print('Year:', current_year)
print('Birthday')
print('Month:', birth_month)
print('Day:', birth_day)
print('Year:', birth_year)

user_age = 0
if (current_month == birth_month and current_day == birth_day):
    print('Happy Birthday!!')
    user_age = current_year - birth_year
elif (current_month < birth_month):
    user_age = current_year - birth_year - 1
elif (current_month == birth_month and current_day > birth_day):
    user_age = current_year - birth_year - 1
else:
    user_age = current_year - birth_year

print('You are', user_age, 'years old.')