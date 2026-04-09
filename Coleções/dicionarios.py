"""
Dicionários
dict = dicionário
Em algumas linguagens de programação os dicionários são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave: valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;
"""
# Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando Elementos

# Foma 1 - Acessando via chave da mesma forma que list/tuple.
print(paises['br'])
print(paises['eua'])
print(paises['py'])
# Obs: Caso tentarmos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError.

# Forma 2 - Acessando via get - Recomendado
print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('py'))
print(paises.get('ru')) # Retorna None

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada.

# Forma 1
# Caso o get não encontre o objeto com a chave informada, será retornado None.
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}.')
else:
    print('Não encontrei o país.')

# Forma 2
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('ru', 'Não encontrado.') # Caso não encontre o país, retorne 'Não encontrado'.
print(pais)

# Podemos verificar se determinada chave se encontra num dicionário.
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) # Retorna False, porque ele não busca por favor, ele busca pela chave.

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado. (int, float, string, boolean) inclusive  lista, tuple dicionário,
# como chaves de dicionários.

# Tuples são interessantes de serem usadas como chave de dicionários, pois são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tóquio',
    (40.7128, 74.0060): 'Escritório na Itália',
    (21.7845, 44.1254): 'Escritório no Canadá',
}
print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 999
print(receita)
print(type(receita))

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado) #OU - receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 700})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados num dicionário é a mesma.
# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Como remover dados de um dicionário

# Forma 1
ret = receita.pop('mai')
print(ret)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é encontrado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']
print(receita)

# Imagine você tem um comércio eletrônico, com um carrinho de compras.
"""
Carrinho de compras:
    Produto 1:
    - nome;
    - quantidade;
    - preço;
    Produto 2:
    - nome;
    - quantidade;
    - preço;
"""

# 1 - Podemos utilizar uma lista para isso? Sim
carrinho = []

produto1 = ['PlayStation 5', 1, 1500.00]
produto2 = ['PlayStation 4', 1, 800.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print(type(carrinho))

# Teríamos que saber qual é o índice de cada informação no produto

# 2 - Podemos utilizar uma tupla para isso? Sim

produto1 = ['PlayStation 3', 1, 400.00]
produto2 = ['PlayStation 2', 1, 150.00]

carrinho = (produto1, produto2)
print(carrinho)
print(type(carrinho))

# Podemos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'The Last Of Us', 'quantidade': 1, 'preço': 100.00}
produto2 = {'nome': 'The Last Of Us Part II', 'quantidade': 1, 'preço': 190.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Desta forma facilmente adicionamos ou removemos produtos no carrinho e em
# cada produto podemos ter a certeza sobre cada informação.

