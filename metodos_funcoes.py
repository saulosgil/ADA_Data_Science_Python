# Métodos de lista

lista = [1,3,12,8,2]

# append

print('Antes do append:', lista)

lista.append(3) # insere o elemento no final da lista
print('Depois do append:', lista)

# insert

lista.insert(2, 10) # insere o elemento na posição escolhida (argumento 2[10])
print('Depois do insert:', lista)

# extend

lista2 = [1,2,3]

lista.extend(lista2)
print('Depois do extend', lista) # insere a nova lista no final da outra lista

# pop

lista.pop() # exclui o ultimo elemento da lista
print('Lista após o pop:', lista) 

lista.pop(0) # exclui o elemento da posição especificada
print('Lista após o pop:', lista) 

# remove

print(lista)

lista.remove(3) # remove o elemento especificado, no caso, o 3 (remove o primeiro que aparece!)
print('Lista após o remove:', lista) 

# count

print('Quantidade de 2 na lista:', lista.count(2)) # conta quantos 2 tem na lista

# index

print(lista)

print('Índice do elemento 12:', lista.index(12)) # mostra a posição de elemento

# sort

print(lista)

lista.sort() # ordena de forma crescente
print(lista)

lista.sort(reverse=True)
print(lista)

# Funções para listas

# len
print(len(lista))

# sum
print('A soma dos elementos da lista é', sum(lista))

# max
print('Maior valor da lista é', max(lista))

# min
print('Menor valor da lista é', min(lista))



