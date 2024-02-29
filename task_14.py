degrees = int(input('N: '))
minutes = 1_440 / 360 * degrees
hours = minutes // 60
print(hours, minutes)
