import pandas as pd
# No lugar dos seus CSVs vou representar aqui dois dataframes
# Os dois têm uma chave de string em comum - a coluna "nome"

# Dataframe1 
dicionario = {"idade": [89, 12, 40, 31],
             "time": ["Portuguesa", "São Paulo", "Flamengo", "Corinthians"],
             "nome_1": ["Joaquim Oliveira", "Carlos da Silva", "Chico dos Santos", "Claudia Schultz"],
                    }
df_1 = pd.DataFrame(dicionario)
print(df_1)

# Dataframe2
dicionario = {"sexo": ["feminino", "masculino", "masculino", "feminino"],
             "veiculo": ["bicicleta", "patinete", "carro", "carro"],
             "nome_2": ["Maria Souza", "Carlos da Silva", "Chico dos Santos", "Claudia Schultz"],
                    }
df_2 = pd.DataFrame(dicionario)
print(df_2)

# Agora eu uno os dois dataframes, apenas nos casos que possuem nomes iguais
novo_df = pd.merge(df_1, df_2, left_on='nome_1', right_on='nome_2')
novo_df.info()
print(novo_df)
#class 'pandas.core.frame.DataFrame'>                                         
#Int64Index: 3 entries, 0 to 2                                                 
#Data columns (total 5 columns):                                               
 #   Column   Non-Null Count  Dtype                                           
#---  ------   --------------  -----                                           
# 0   idade    3 non-null      int64                                           
# 1   time     3 non-null      object                                          
# 2   nome     3 non-null      object                                          
 #3   sexo     3 non-null      object                                          
# 4   veiculo  3 non-null      object                                          
#dtypes: int64(1), object(4)                                                   
#memory usage: 96.0+ bytes  
#Aqui mais sobre a documentação 1 do merge

