#Alexander Ho
#1677933

print('''Davy's auto shop services''')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wax': 12}
print('')

total = 0
print('Select first service:')
first_service = input()
print('Select second service:')
second_service = input()
print('')
print('''Davy's auto shop invoice''')
print('')

if (first_service == '-'):
    print('Service 1: No service')
else:
    for sel_ser in services:
        if (first_service == sel_ser):
            print('Service 1: ' + sel_ser + ', $' + str(services[sel_ser]))
            total += services[sel_ser]

if (second_service == '-'):
    print('Service 2: No service')
else:
    for sel_ser in services:
        if (second_service == sel_ser):
            print('Service 2: ' + sel_ser + ', $' + str(services[sel_ser]))
            total += services[sel_ser]
print('')
print('Total: $' + str(total))

