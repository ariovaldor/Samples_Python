import pandas as pd

#Leitura dos arquivos
# Para funcionar, tive também que instalar a biblioteca openpyxl
df1 = pd.read_excel("d:/Ari_ESTUDOS/PHYTON/DATASETS/Aracaju.xlsx")
df2 = pd.read_excel("d:/Ari_ESTUDOS/PHYTON/DATASETS/Fortaleza.xlsx")
df3 = pd.read_excel("d:/Ari_ESTUDOS/PHYTON/DATASETS/Natal.xlsx")
df4 = pd.read_excel("d:/Ari_ESTUDOS/PHYTON/DATASETS/Recife.xlsx")
df5 = pd.read_excel("d:/Ari_ESTUDOS/PHYTON/DATASETS/Salvador.xlsx")
#Concatenando todos os arquivos em um único data frame
df = pd.concat([df1,df2,df3,df4,df5])

#Exibindo 5 primeiras linhas

print(df.head())