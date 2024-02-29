number_x = int(input('X: '))
number_y = int(input('Y: '))
number = (number_x % number_y)*(number_y % number_x) + 1
print(number)
