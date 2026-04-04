"""
and (e), or (ou), not (nao), is (é)

operadores unários:
    not
operadores binários:
    and, or, is

Para o 'end', ambos valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor é invertido

"""
ativo = True
logado = True

# and
if ativo and logado:
    print('O usuário está ativo no sistema')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail.')

# is
ativo = False
logado = True

if ativo is True:
    print('O usuário está ativo no sistema')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail.')

#not
ativo = False
logado = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail.')
else:
    print('O usuário está ativo no sistema')