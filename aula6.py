# aula 6 Conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao =conjunto.union(conjunto2)
print(type(conjunto_uniao))
print(conjunto_uniao)
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {} '.format(conjunto_diferenca2))
conjun_dif_simetr = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica:{}' .format(conjun_dif_simetr))