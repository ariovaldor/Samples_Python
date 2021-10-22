# aula7b Métodos
class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b
if __name__ == '__main__':
    calculo = Calculadora()
    print(calculo.soma(20,30))
    print(calculo.subtracao(10,5))
    print(calculo.multiplicacao(1540,120))
    print(calculo.divisao(365021,78960))