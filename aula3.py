# Imprimir todos os números primos de 0 a 100
# i varia de zero a 100
for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
    #    print(x,resto,)
        if resto == 0:
            div = div+1
    if div == 2:
        print(num)
