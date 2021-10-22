class Televisao:
    def __init__(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

teve = Televisao()
print('Televisâo está ligada ? {}' .format(teve.ligada))
# Chamei método power
teve.power()
print('Apertei Power ')
print('Televisâo está ligada ? {}' .format(teve.ligada))
# Chamei método power
teve.power()
print('Apertei Power ')
print('Televisâo está ligada ? {}' .format(teve.ligada))
