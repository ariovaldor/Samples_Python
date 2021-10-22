import pandas as pd
import pandera as pa
# carregar frame convertendo datas para o formato correto
df = pd.read_csv('D:/Ari_ESTUDOS/PHYTON/etl/ocorrencia.csv', sep=";", parse_dates=(['ocorrencia_dia']),dayfirst=True)
print(type(df))
print(df.dtypes)
#agora posso fazer referencia a coluna cabaçalho do dataframe
# no print vem as cinco primeiras linhas e as cinco últimas
print(df.ocorrencia_dia)
# Agora monto os schemas para validat tipo de dado de cada coluna
# pa.Int verifica se é inteiro, pa.Datetime verifica se é data válida
schema =pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia":pa.Column(pa.Int),
        "codigo_ocorrencia1":pa.Column(pa.Int),
        "ocorrencia_classificacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String, pa.Check.str_length(2,2)),
        "ocorrencia_aerodromo":pa.Column(pa.String),
        "ocorrencia_dia":pa.Column(pa.DateTime,nullable=True),
        "ocorrencia_hora":pa.Column(pa.String,pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),

        "total_recomendacoes":pa.Column(pa.Int)

    }
)
schema.validate(df)
df
