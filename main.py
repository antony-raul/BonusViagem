import pandas as pd
#abrir arquivos em Excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
path = 'C:/Users/raulz/Downloads/Arquivos/'
for mes in  lista_meses:
    tabela_vendas = pd.read_excel(f'{path}{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'Vendedor {vendedor} bateu a meta, fez {vendas} vendas no mês de {mes}')


