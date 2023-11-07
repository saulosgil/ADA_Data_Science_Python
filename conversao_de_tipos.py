# CONVERSÃO DE TIPOS

idade = '26'
numero1 = '10'
numero2 = '20'

print(numero1 + numero2) # neste caso o Python entende que ambos são strings faz uma concatenação

# Converter str para int

## verificando o tipo da variável com type
idade = '26'

print(idade, type(idade))

## Convertendo para inteiro com a fct int() e imprimindo novamente

idade_inteira = int(idade) 

print(idade_inteira, type(idade_inteira))

# outros conversores

# int( )
# str()
# float()
# bool()

# Exemplo
# str para float
altura = float(input('Informe sua altura: '))

print(altura, type(altura))





