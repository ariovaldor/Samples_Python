import pandas as pd
df1 = pd.DataFrame({'l_key': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'r_key': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})
print(df1)
print(df2)

# Fazer o merge de df1 e df2 usando as chaves lkey e rkey
# Os cabeçalhos são anexados dos sufixos '_left' e '_right'
result = df1.merge(df2, left_on='l_key', right_on='r_key', suffixes=('_left', '_right'))

print(result)
  