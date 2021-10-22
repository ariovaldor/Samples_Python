import  pandas as pd
df = pd.read_csv('D:/Ari_ESTUDOS/PHYTON/etl/ocorrencia.csv', sep=";", parse_dates=(['ocorrencia_dia']),dayfirst = True)
print(df.loc[1,'ocorrencia_cidade'])
print(df.loc[3])
print(df.loc[1:3])
#ver todas as linhas de uma coluna
print(df.loc[:,'ocorrencia_cidade'])
# saber se uma coluna tem valores unicos
df.codigo_ocorrencia.is_unique
# determinar que uma coluna passe a ser indice
df.set_index('codigo_ocorrencia')
# resetar indice original
df.reset_index(drop=True, inplace=True)

# alterar uma celula com "****" para vazia
df.loc[0,'ocorrencia_aerodromo']=''