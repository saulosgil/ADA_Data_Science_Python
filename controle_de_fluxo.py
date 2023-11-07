# Estrutura de controle de fluxo
# Condicionais

idade = 10

if idade >= 18:
  print('Você é maior de idade.')
else:
  print('Você é menor de idade.')

"""
Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média superior 
ou iguala 7, e "Reprovado(a)", caso a média seja inferior a 7.
"""

media = float(input('Informe a média do estudante: '))


if media >= 7:
  print('Você foi aprovado(a)!')
elif media >= 5:
  print('Recuperação')
else:
  print('Você foi reprovado(a)!')

# aumentando a complexidade - Reprovação por presença usando a 'and'

media = float(input('Informe a média do estudante: '))

media = 10
presenca = 5

if media >= 7 and presenca >= 70:
  print('Aprovado(a)!')
  print('Parabéns!!!')
else:
  print('Reprovado!')
  print('Tente novamente.')














