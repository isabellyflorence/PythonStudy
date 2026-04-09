"""
Ranges

- Precisamos entender o loop for para usar o range.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória,
mas sim de maneira especificada

Formas gerais:

#Forma 1

range(valor_final)

OBS: valor_final não inclusive (início padrão de 0, e passo de 1 em 1)

#Exemplo Forma 1

for num in range(11):
    print(num)

#Forma 2

range(valor_inicial, valor_final)

OBS: valor_final não inclusive (início especificado pelo usuário, e passo de 1 em 1)

#Exemplo Forma 2

for num in range(1, 11):
    print(num)

#Forma 3

range(valor_inicial, valor_final, passo)

OBS: valor_final não inclusive (início especificado pelo usuário, e passo especificado pelo usuário))

#Exemplo Forma 3

for num in range(1, 10, 2):
    print(num)

#Forma 4 (Inversa)

range(valor_inicial, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário))

#Exemplo forma 4

for num in range(10, 0, -1):
    print(num)
"""
