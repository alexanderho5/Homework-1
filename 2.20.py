#Alexander Ho
#1677933

print('Enter amount of lemon juice (in cups):')
num_lemonjuice = int(input())
print('Enter amount of water (in cups):')
num_water = int(input())
print('Enter amount of agave nectar (in cups):')
num_agave = float(input())
print('How many servings does this make?')
servings = int(input())
print('')

print('Lemonade ingredients - yields', f'{servings:.2f}', 'servings')
print(f'{num_lemonjuice:.2f}', 'cup(s) lemon juice')
print(f'{num_water:.2f}', 'cup(s) water')
print(f'{num_agave:.2f}', 'cup(s) agave nectar')
print('')
print('How many servings would you like to make?')
print('')
servingstobeconverted = int(input())
print('Lemonade ingredients - yields',f'{servingstobeconverted:.2f}','servings')
print(f'{servingstobeconverted/3:.2f}', 'cup(s) lemon juice')
print(f'{servingstobeconverted * 8/3:.2f}', 'cup(s) water')
print(f'{servingstobeconverted/2.4:.2f}', 'cup(s) agave nectar')
print('')
print('Lemonade ingredients - yields',f'{servingstobeconverted:.2f}','servings')
print(f'{(servingstobeconverted/3)/16:.2f}', 'gallon(s) lemon juice')
print(f'{(servingstobeconverted * 8/3)/16:.2f}', 'gallon(s) water')
print(f'{(servingstobeconverted/2.4)/16:.2f}', 'gallon(s) agave nectar')
