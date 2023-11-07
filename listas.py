# LISTAS

# Antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com lista
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = [] # lista vazia
lista = list() # outro jeito de criar lista
lista = [26, 'Walisson', 3.14159, False]
lista_de_listas = [10,[1,2,3]]

# Indexação e Slices (fatiamento)

lista = [26, 'Walisson', 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) # acessa a lista de trás para frente, neste caso True

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # seleciona os itens da posição zero a terceira 
print(lista[3:4])
print(lista[3:]) # seleciona a posição 3 até o final da lista
print(lista[0:6:2]) # seleciona da posição 2 até a 6 pulando de 2 em 2

# Iterações com FOR

# 1. utilizando os próprios elementos da lista

for elemento in lista:
  print(elemento)

# 2. utilizando os índices

print('O comrpimento da lista é de', len(lista), 'elementos')

for i in range(len(lista)):
  print(i)