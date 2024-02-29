attempts = float(input('ATT: '))
if attempts < 0 or attempts > 2.375:
    print('Mistake.')
else:
    completions = float(input('CMP: '))
    if completions < 0 or completions > 2.375:
        print('Mistake.')
    else:
        yards = float(input('YDS: '))
        if yards < 0 or yards > 2.375:
            print('Mistake.')
        else:
            touchdown = float(input('TD: '))
            if touchdown < 0 or touchdown > 2.375:
                print('Mistake.')
            else:
                interceptions = float(input('INT: '))
                if interceptions < 0 or interceptions > 2.375:
                    print('Mistake.')
                else:
                    calculation_a = (completions/attempts - 0.3) * 5
                    if calculation_a > 2.375:
                        calculation_a = 2.375
                    elif calculation_a < 0:
                        calculation_a = 0
                    calculation_b = (yards/attempts - 3) * 0.25
                    if calculation_b > 2.375:
                        calculation_b = 2.375
                    elif calculation_b < 0:
                        calculation_b = 0
                    calculation_c = (touchdown/attempts) * 20
                    if calculation_c > 2.375:
                        calculation_c = 2.375
                    elif calculation_c < 0:
                        calculation_c = 0
                    calculation_d = 2.375 - (interceptions/attempts*25)
                    if calculation_d > 2.375:
                        calculation_d = 2.375
                    elif calculation_d < 0:
                        calculation_d = 0
                    passer_rating = ((calculation_a+calculation_b+calculation_c+calculation_d) / 6) * 100
                    print('Passer rating: ', round(passer_rating, 1))
