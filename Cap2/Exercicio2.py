numero = int(input('Qual tabuada voce quer ver? '))
inicio = int(input('Qual o inicio do intervalo? '))
fim = int(input('Qual o final do intervalo? '))

for c in range(inicio, fim + 1):
    print('{} x {} = {}'.format(numero, c, numero * c))