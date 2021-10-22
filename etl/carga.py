import pandas as pd
#df = pd.read_csv('ocorrencia.csv', sep=";")
# carregar frame convertendo datas para o formato correto
df = pd.read_csv('D:/Ari_ESTUDOS/PHYTON/etl/ocorrencia.csv', sep=";", parse_dates=(['ocorrencia_dia']),dayfirst=True)
print(type(df))
print(df.dtypes)
#agora posso fazer referencia a coluna cabaçalho do dataframe
# no print vem as cinco primeiras linhas e as cinco últimas
print(df.ocorrencia_dia)