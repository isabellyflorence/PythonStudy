"""
Recebendo dados do Usuário

input() -> Todo dado recebido via input é String
"""
# Entrada de dados
print('Qual o seu nome?')
nome = input()

print('Seja bem-vindo(a) %s' % nome)

print('Qual a sua idade?')
idade = input()

# Saída de dados
print('%s tem %s anos de idade' % (nome, idade))


# FORMA MODERNA

print('Qual o seu nome?')
nome = input()

print('Seja bem-vindo(a) {0}'.format(nome))

print('Qual a sua idade?')
idade= input()

print('{0} tem {1} anos de idade'.format(nome, idade))

# FOMA MAIS MODERNA AINDA

print('Qual o seu nome?')
nome = input()

print(f'Seja bem-vindo(a) {nome}')

print('Qual a sua idade?')
idade= input()

print(f'{nome} tem {idade} anos de idade')
print(f'{nome} tem {idade} anos de idade e nasceu em {2026 - int(idade)}')