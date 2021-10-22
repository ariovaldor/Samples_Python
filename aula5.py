#Tuplas e Listas
numeros = [1, 3, 5, 7]
animais = ['cachorro', 'gato','elefante']
print(type(numeros))
print(numeros)
print(animais)
for x in animais:
    print(x)
soma = 0
for x in numeros:
    print(x)
    soma +=x
    print(soma)
if 'gato' in animais:
    print('Existe um gato na Lista')
else:
    print('Não existe gato na Lista')