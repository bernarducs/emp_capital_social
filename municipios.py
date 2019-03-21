import pandas as pd

df = pd.read_excel('municipios.xlsx')

for m in df['nm_municipio']:
    novo_nome = m.replace(" ", "-").upper()
    print(novo_nome)
