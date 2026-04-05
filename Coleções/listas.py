"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays), com a diferença de serem
DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java
    - Arrays possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, esse array
    será SEMPRE do tipo inteiro e poderá SEMPRE no máximo 5 valores.

Python
- Dinâmico: Não possui tamanho fixo, ou seja, podemos criar a lista e ir adicionando elementos
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado

As listas são representadas por colchetes []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1 ,44, 42, 27]

lista2 = ['i', 's', 'a', 'b', 'e', 'l', 'l', 'y']

lista3 = []

lista4= list(range(11))

lista5 = list('isabelly florence')

# Podemos facilmente checar se determinado valor está contido na lista
num = 5

if num in lista4:
     print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordernar uma lista
lista1.sort()
print(lista1)

#String
lista5.sort()
print(lista5)

# Podemos contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('l'))

# Adicionar elementos em listas
"""
Para adicionar elementos em listas, utilizamos a função append
Com append, nós só conseguimos adicionar 1 elemento por vez
"""

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) # Adicionado a lista como um elemento único
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a Lista')
else:
    print('Não encontrei a Lista')

lista1.extend([23, 44, 67]) # Adicionado os elementos individualmente, e ele não aceita valores únicos.
print(lista1)

# Podemos inserir um novo elemento a lista informando a posição do índice
# Isso não substitui o valor inicial, ele só será deslocado para a direita
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Ou
lista1.extend(lista2)
print(lista1)

# Podemos inverter uma lista
lista1.reverse()
print(lista1)

# Ou
print(lista1[: : -1])
print(lista2[: : -1])
print(lista3[: : -1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista6))

# Podemos remover o último elemento de uma lista
# O pop não somente remove o último elemento mas também retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover o elemento pelo índice
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista
nova = [1, 2 ,3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter string para uma lista

#Exemplo 1
curso = 'Python Avançado'
print(curso)
curso = curso.split()
print(curso)

#Exemplo 2
curso = 'Python, do , Básico, ao, Avançado'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma Lista em uma String
lista7 = ['Python', 'do', 'Básico', 'ao', 'Avançado']
print(lista7)

# Abaixo estamos falando, pega a lista7 coloca espaço entre cada elemento
# e transforma em uma string
curso = ' '.join(lista7)
print(curso)

# Abaixo estamos falando pega a lista7, e coloca um cifrão entre cada elemento
curso = '$'.join(lista7)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista8 = [1, 2, 3.4, True, 'isa', 's', [1, 2, 3], 33333]
print(lista8)
print(type(lista8))

# Iterando sobre listas

#Exemplo 1 - Utilizando for
soma = 0
lista1 = [1, 99, 4, 27, 15, 22, 3, 1 ,44, 42, 27]
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

#Exemplo 2 em String - Utilizando for
soma = ''
lista2 = ['i', 's', 'a', 'b', 'e', 'l', 'l', 'y']
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)
"""
#Exemplo 3 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair")
    produto = input("Digite o nome do produto: ")
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
"""
# Podemos criar listas com variáveis
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

# Em listas fazemos acesso aos elementos de forma indexada
#           0         1        2
cores = ['verde', 'amarelo', 'azul']
print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul

# Podemos fazer acesso aos elementos de forma indexada inversa
#           0         1        2
cores = ['verde', 'amarelo', 'azul']
print(cores[-1]) #azul
print(cores[-2]) #amarelo
print(cores[-3]) #verde
# print(cores[-4]) Erro, pois não tem índice -5


cores = ['verde', 'amarelo', 'azul']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Podemos gerar índices em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(1)
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(2)
print(lista)

# Outros métodos para listas

#Encontrar o índice de um elemento na lista

numeros = [1, 2, 3, 4, 10, 5, 6, 7, 8, 9, 10]

#Em qual índice da lista está o valor 6?
print(numeros.index(6))

#Em qual indice da lista está o valor 9?
print(numeros.index(9))

# No caso de dois elementos iguais, retorna o índice do primeiro elemento encontrado
print(numeros.index(10))

#obs: caso não tenha o elemento na lista, apresentará erro

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(10, 5)) # buscando a partir do índice 5

# Podemos fazer busca dentro de um range, início/fim
print(numeros.index(5, 2, 8)) # buscar o índice 5, entre os valores 2 e 8

# Revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slicing de listas com parâmetro 'início'
#        0  1  2  3
lista = [1, 2, 3 ,4]

print(lista[:]) #pegando todos os elementos
print(lista[1:]) #iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slicing de listas com parâmetro 'fim'
print(lista[1:2]) #iniciando no índice 1 e terminando no índice 2
print(lista[:2]) #iniciando no índice 0 e terminando no índice 2

# Trabalhando com slicing de listas com parâmetro 'passo'
print(lista[1::2]) #iniciando no índice 1 e vai até o final de 2 em 2
print(lista[::2]) #iniciando no índice 0 e vai até o final de 2 em 2
print(lista[1::-1]) #inverte os valores começando de trás para frente

# Podemos inverter valores
nomes = ['Isabelly', 'Florence']
nomes[0],nomes[1] = nomes[1],nomes[0]
print(nomes)

# Ou
nomes = ['Isabelly', 'Florence']
nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista9 = [1, 2, 3, 4, 5, 6]

print(sum(lista9)) #soma
print(max(lista9))  #máximo valor
print(min(lista9))  #mínimo valor
print(len(lista9))  #tamanho da lista

# Podemos transformar uma lista em tupla
lista10 = [1, 2, 3, 4, 5, 6]

print(lista10)
print(type(lista10))

tupla = tuple(lista10)
print(tupla)
print(type(tupla))

# Podemos copiar uma lista para outra lista

#Forma1
lista12 = [1, 2, 3]
print(lista12)

nova1 = lista12.copy()
print(nova1)

nova1.append(4)
print(lista12)
print(nova1)

# Ao utilizarmos lista12.copy(), copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista não afeta a outra
# Isso em python é chamado de Depp Copy (cópia profunda).

#Forma2 - Shallow Copy
lista13 = [1, 2, 3]
print(lista13)

nova2 = lista13 #copia
print(nova2)

nova2.append(4)

print(lista13)
print(nova2)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista
# para a nova lista, mas após realizar modificação em uma das listas, essa modificação
# se refletiu em ambas as listas.
# Isso em Python se chama Shallow Copy

