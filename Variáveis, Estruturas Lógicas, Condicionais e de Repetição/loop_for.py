"""
Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in iterável:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
-String
    nome = 'Isabelly'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    números = range(1, 10)

# Enumerate

((0, 'i'), (1, 's'), (2, 'a'), (3, 'b'), (4, 'e'), (5, 'l'), (6, 'l'), (7, 'y'))

for indice, letra in enumerate(numeros):
    print(nome[indice])

for indice, letra in enumerate(numeros):
    print(letra)

for _, numero in enumerate(numeros):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo usando underline _

nome = 'Isabelly Florence'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

#Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

#Exemplo de for 2 (iterando em uma lista)
for numero in lista:
    print(numero)

#Exemplo de um for 3 (iterando em um range)

range(valor_inicial, valor final)

OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)

#Enumerate

for valor in enumerate(nome):
    print(valor)



qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

nome = 'Isabelly Florence'
for letra in nome:
    print(letra)

Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode


#Original: U+1F60D
#Modificado: U0001F60D

for _ in range(3):
        for num in range(1, 11):
            print('\U0001F60D' * num)
"""