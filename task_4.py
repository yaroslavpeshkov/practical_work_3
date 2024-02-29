import ru_local as ru
rubles_x, kopeck_y, amount_n = map(int, input().split())
price = float(str(rubles_x) + "." + str(kopeck_y))
revenue = price * amount_n
rubles_r, kopeck_k = map(int, str(format(revenue, '.2f')).split('.'))
print(f'{rubles_r} {ru.RUB} {kopeck_k} {ru.KOP}')
