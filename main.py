import requests
from bs4 import BeautifulSoup
import pandas as pd

df_municipios = pd.read_excel('municipios.xlsx')

lista_de_empresas = []

for m, cod in zip(df_municipios['municipio_sem_acentos'], df_municipios['cd_municipio']):
    nm_municipio = m.upper()
    novo_nome_municipio = nm_municipio.replace(" ", "-")

    url = 'https://www.econodata.com.br/lista-empresas/PERNAMBUCO/' + novo_nome_municipio

    # tabela via pandas, nome das empresas saem com url, aqui só pegaremos o capital social
    base = pd.read_html(url)
    df = base[0]

    # requests para obter o nome da empresa
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'html.parser')

    # printa html
    # print(sp.prettify())

    cl = sp.find_all(class_='underline')

    for empresa, vlr in zip(cl, df['Capital Social']):
        lista = []
        lista.append(cod)
        lista.append(nm_municipio)
        lista.append(empresa.text)
        lista.append(vlr)
        lista_de_empresas.append(lista)

    print(lista_de_empresas)

colunas = ['municipio', 'nm_empresa', 'capital_social']
df_empresas = pd.DataFrame(lista_de_empresas, columns=colunas)

df_empresas.to_csv('empresas_cap_social_pe.csv', sep=',', header=True)
