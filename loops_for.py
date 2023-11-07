# laços de repetição - FOR

# range de 10, ou seja, de zero a 10 (não inclusivo)
for  variavel in range(10):
  print(variavel)

# range de 10, ou seja, de cinco a 15 (não inclusivo)
# - primeiro argumento - inicio
# - segundo argumento - final
for  variavel in range(5, 15):
  print(variavel)

# range de 10, ou seja, de cinco a 15 (não inclusivo) pulando de 3 em 3
# - primeiro argumento - inicio
# - segundo argumento - final
# - terceiro argumento pula de quando em quanto

for  variavel in range(0, 12, 3):
  print(variavel)

  # Exemplo

"""
nota1 = float(input('Informe sua nota 1: '))
nota2 = float(input('Informe sua nota 2: '))
nota3 = float(input('Informe sua nota 3: '))
"""

soma = 0

for i in range(1, 4):
  nota = float(input(f'Informe a sua nota {i}'))

  soma = soma + nota

print(soma / 3)


