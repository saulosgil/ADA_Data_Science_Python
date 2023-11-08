# 
# 1. O que são funções e por que utilizá-las?

# Funções que já utilizados anteriormente

"""
print() # imprimi uma mensagem no console/terminak/cmd
input() # Retorna um dado informado pelo usuário
len() # recebe uma lista e retorna o tamanho da lista
max() # retorna o maior valor de uma lista
"""


# 2. Criação de funções

# Função inicial
## define a função
def saudacao():
  print('Seja bem-vindo(a)!')
  print('Olá, é um prazer ter você fazendo parte desse curso!')

## Chama a função
saudacao()

# Função com parâmetros
def saudacao(nome, curso='Python'):
  print(f'Seja bem-vindo(a),{nome}!')
  print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao(nome='Walisson',curso='Python')

# Função com paramêtro defaul
def saudacao(nome, curso='Python'):
  print(f'Seja bem-vindo(a),{nome}!')
  print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao(nome='Walisson') # se não passar o argumento curso, o default é Python
saudacao(nome='Walisson', curso='C++')

 #  Funções com retorno
def soma(num1, num2):
  return num1 + num2

resultado = soma(5, 7)

print(resultado)

# Exemplo 2 - calculadora

def calculadora(num1, num2, operacao='+'):
  if operacao == '+':
    return num1 + num2
  elif operacao == '-':
    return num1 - num2
  elif operacao == '*':
    return num1 * num2
  elif operacao == '/':
    return num1 / num2
  
calculadora(1, 2, operacao='+')
calculadora(1, 2, operacao='-')
calculadora(1, 2, operacao='*')
calculadora(1, 2, operacao='/')
