# Dicionários

 # # Criando dicionários

dicionario = {}
dicionario = dict() # função para criar dicionário vazio

dicionario = {'nome': 'Walisson', 'idade': 26, 'altura': 1.77}
print(dicionario)

# Acessando os elementos pela chave
print(dicionario['idade'])

# Adicionando elementos no dicionário

dicionario['programador'] = True
print(dicionario)

# Sobrescrever um elemento

print(dicionario) # dicionário até este momento

dicionario['altura'] = 2

print(dicionario) # dicionário após a alteração da altura

# Iterando sobre um dicionario

for variavel in dicionario: # por padrão ele pega as chaves
  print(variavel)

for chave in dicionario: # pegando a chave e os valores
  print(f'{chave}:{dicionario[chave]}')

# Testando a existência de uma chave

print('peso' in dicionario) # testa se peso a chave existe
print('altura' in dicionario) # testa se peso a chave existe