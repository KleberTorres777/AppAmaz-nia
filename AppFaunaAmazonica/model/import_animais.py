import pandas as pd

# Lê o arquivo CSV e o armazena em um DataFrame
dataframe = pd.read_csv(r'//dados_animais.csv')

print(dataframe.head(9))


