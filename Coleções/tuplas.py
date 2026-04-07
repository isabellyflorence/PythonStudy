"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupula ela não muda.
    Toda a operação em uma tupla gera uma nova tupla.

# Por que utilizar tuplas?

# - Tuplas são mais rápidas que listas.
# - Tuplas deixam o seu código mais seguro, por ser imutáveis.

"""
# Cuidado 1: As tuplas são representas por parêntes, mas veja:

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

tuple2 = 1, 2, 3, 4, 5
print(tuple2)
print(type(tuple2))

# Cuidado 2: Tuplas com 1 elemento

tuple3 = (4) # Isso não é uma tupla
print(tuple3)
print(type(tuple3))

tuple4 =(4,) # Isso é uma tupla
print(tuple4)
print(type(tuple4))

tuple5 = 4,
print(tuple5)
print(type(tuple5))

# Conclusão: Tuplas são definidas pelo uso da vírgula e não somente pelos parênteses

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tuple = tuple(range(5))
print(tuple)
print(type(tuple))

# Desempacotamento de tupla

tuple6 = ('Isabelly', 'Florence')
nome, sobrenome = tuple6
print(nome)
print(sobrenome)

# Gera erro se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos na tuplas não existem, dado o fato de serem imutáveis.

# *Soma, Valor Máximo*, Valor Mínimo* ou Reais
# * Se os valores forem todos inteiros ou reais

tuple7 = (1, 2, 3, 4, 5)
print(sum(tuple7))
print(max(tuple7))
print(min(tuple7))
print(len(tuple7))

# Concatenação de tuplas

tuple8 = (1, 2, 3, 4, 5)
print(tuple8)

tuple9 = (6, 7, 8, 9, 10)
print(tuple9)

print(tuple8 + tuple9) # Tuplas são imutáveis
print(tuple8)
print(tuple9)

tuple8 = tuple8 + tuple9 # Tuplas são imutáveis, mas podemos sobrescrever os seus valores
print(tuple8)

# Verificar se determinado elemento está contido na tupla

tuple10 = (1, 2, 3)
print(3 in tuple10) # True ou False

tuple11 = (1, 2 ,3)

# Iterando sobre uma tupla

for n in tuple11: # Para cada número nessa tupla, imprime esse número
    print(n)

for indice, valor in enumerate(tuple11): # Imprime o valor e seu índice
    print(indice, valor)

# Contando elementos numa tupla

tuple12 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tuple12.count('a'))

nome = 'isabelly florence'
print(nome)
print(nome.count('l'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisamos modificar os dados em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# Acessos a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual indice um elemento está na tupla

print(meses.index('Maio'))
# Obs: Caso o elemento não exista, dará erro

# Slicing

# tupla[inicio:fim:passo}

print(meses[5:9])

# Copiando uma tupla para outra

tuple13 = (1, 2, 3, 4, 5)
print(tuple13)

nova = tuple13 # Na tupla não temos o problema de Shallow Copy
print(nova)
print(tuple13)

outra = (6, 7 , 8)
nova = nova + outra
print(nova)
print(tuple13)

