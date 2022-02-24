import pandas as pd
from twilio.rest import Client

path = 'C:/Users/raulz/Downloads/Arquivos/'
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
account_sid = 'ACc186ccd6e63519fb4d1f00268ac14704'
auth_token = '0a5d823a4124a35f2790867201e0d36d'
metas = []
client = Client(account_sid, auth_token)

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{path}{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values
        for i in range(len(vendedor)):
            metas.append(
                f'Vendedor(a) {vendedor[i]} bateu a meta, fez {vendas[i]} vendas no mês de {mes}')

for j in range(len(metas)):
    message = client.messages.create(
        messaging_service_sid='MG57bafc18f8a1041e6c2df2b2483558d2',
        body=metas[j],
        to='+5588996483056',
        from_='+19032963885'
    )
