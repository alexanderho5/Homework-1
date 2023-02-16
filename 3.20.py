#Alexander Ho
#1677933

import math

print('Enter wall height (feet):')
wall_height = int(input())
print('Enter wall width (feet):')
wall_width = int(input())
wall_area = wall_width * wall_height
print('Wall area:', wall_area, 'square feet')

print('Paint needed:', f'{wall_area/350:.2f}', 'gallons')
cans_needed = math.ceil(wall_area/350)

print('Cans needed:', cans_needed, 'can(s)')

print('')

wall_color = str(input())
paint_color = {'red': 35, 'blue': 25, 'green':23}
print('Choose a color to paint the wall:')
print('Cost of purchasing {} paint:'.format(wall_color),'${}'.format(paint_color[wall_color]*cans_needed))
