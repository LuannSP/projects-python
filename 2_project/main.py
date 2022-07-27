"""
    Projeto 2: (Até 26% dos clientes fizeram 'Churn' do serviço, por que?)

    Passo 1: Importar a base de dados
    Passo 2: Visualizar a base de dados
    Passo 3: Organizar a base de dados (Tratamento de dados)
    Passo 4: Análise incial dos dados
    Passo 5: Descobrir os motivos do cancelamento dos clientes
"""

# Remover informações inútil (informação que não te ajuda, te atrapalha!)
# Axis = 0 -> eixo da linha
# Axis = 1 -> eixo da coluna

import pandas as pd
import plotly.express as px

table = pd.read_csv(r'database//telecom_users.csv')

# Excluindo coluna inútil
table = table.drop('Unnamed: 0', axis=1)
table = table.drop('IDCliente', axis=1)

# Arrumando o tipo da coluna
# Opções de errors: coerce: forçar a operação, raise: abortar a operação, ignore: ignorar o error.
table['TotalGasto'] = pd.to_numeric(table['TotalGasto'], errors='coerce')

# Excluir colunas completamente vazias
table = table.dropna(how='all', axis=1)

# Excluir linhas vazias que tem alguma coluna vazia
# (de 5968 linhas, 10 estão vazias, então posso pagar as 10)
table = table.dropna(how='any', axis=0)

# Verificando se realmente são 26%
# print(
#     table['Churn'].value_counts(),
#     table['Churn'].value_counts(normalize=True).map('{:.1%}'.format),
#     sep='\n'
# )

# Relacionando todas as tabelas com a de 'Chrun' e criando gráfico
for column in table.columns:
    if column != 'Churn':
        graphic = px.histogram(table, x=column, color='Churn', text_auto=True)
        graphic.show()

# Conclusões:
#   - Clientes com poucos meses de serviço desistem muito rapido do serviço
#   - Clientes que usam o BoletoEletronico tendem a cancelar mais o serviço
#   - Clientes com contrato mensal tendem a cancelar muito mais o serviço
#   - Quantos mais serviços o cliente tem, menor a chance dele cancelar
#   - Cliente com uma família maior, tendem a ter um menor cancelamento
