nome = input('Qual o seu nome completo? ')

print('Maiúsculas:', nome.upper())
print('Minúsculas:', nome.lower())

nome_sem_espacos = nome.replace(' ', '')
print('Total de letras:', len(nome_sem_espacos))

partes = nome.split()
ultimo_nome = partes[len(partes) - 1]
nome_modificado = nome.replace(ultimo_nome, 'do Inatel')

print('Nome modificado:', nome_modificado)