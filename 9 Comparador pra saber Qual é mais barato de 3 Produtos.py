



prod_1 = float(input('Valor 1° produto: R$: ' ))
prod_2 = float(input('Valor 2° produto: R$: '))
prod_3 = float(input('Valor 3° produto: R$: '))

if prod_1 <= prod_2 and prod_1 <= prod_3:
    print(f'Compre o primeiro produto Por {prod_1:,.0f} Reais\n')
elif prod_2 <= prod_3:
    print(f'Compre o segundo produto Por {prod_2:,.0f} Reais\n')
else:
    print(f'Compre o terceiro produto Por {prod_3:,.0f} Reais\n')

