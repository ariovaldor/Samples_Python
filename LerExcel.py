import numpy as np

import pandas as pd

#Efetuando a Leitura dos dados da Planilha MS-EXCEL 'CariocaFutebol.xls'
dado = pd.read_excel('D:\Ari_ESTUDOS\PHYTON\Projetos\Exercicios/CariocaFutebol.xlsx')
print(dado)
#Criando o array idade transformados para o tipo int (os campos numéricos da planilha são carregado como float)
idade = np.array(dado['Idade']).astype(int)

#Criando a série jogadores com o campo de valores idades e campo índices nomes
jogadores = pd.Series(idade, index=dado['Nome'])

#Exibindo os últimos 5 elementos da Série
print(jogadores)
jogadores.tail()