sexo = input('Digite seu sexo (M ou F): ')
sexo = sexo.upper()

while sexo != 'M':
    if sexo == 'F':
        break
    sexo = input('Invalido. Digite seu sexo (M ou F): ')
    sexo = sexo.upper()

if sexo == 'M':
    print('Voce é homem')
else:
    print('Voce é mulher')