"""
Loop While

Forma Geral

While expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é Verdadeiro ou Falso. (True or False).

Ex:

num = 5

num < 5

#Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero += 1 #Critério de parada

# OBS: Em um loop while, é importante que cuidemos do critério de parada. Para
# não causar um loop infinito
"""

#Exemplo 2

reposta = ''

while reposta != 'sim':
    reposta = input('Já acabou Jéssica? ')
