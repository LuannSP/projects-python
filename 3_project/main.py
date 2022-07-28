"""
    Project 3:

    Passo 1: Pegar cotação do dolar, euro e ouro
    Passo 2: Atualizar a base de dados
    Passo 3: Recalcular os preços
    Passo 4: Exportar a base de dados
"""

# .send_keys() - Escrever
# .click() - Clicar
# .get() - Pegar

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()

# Dolar
browser.get('https://www.google.com.br/')
browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação do dólar', Keys.ENTER)
dolar = browser.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Euro
browser.get('https://www.google.com.br/')
browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação do euro', Keys.ENTER)
euro = browser.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Ouro
browser.get('https://www.melhorcambio.com/ouro-hoje')
ouro = browser.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
ouro = ouro.replace(',', '.')

browser.quit()

# Base de dados
table = pd.read_excel(r'database//Produtos.xlsx')

# table.loc[linha, coluna] = valor
table.loc[table['Moeda'] == 'Dólar', 'Cotação'] = float(dolar)
table.loc[table['Moeda'] == 'Euro', 'Cotação'] = float(euro)
table.loc[table['Moeda'] == 'Ouro', 'Cotação'] = float(ouro)

# Atualizando os preços
table['Preço de Compra'] = table['Preço Original'] * table['Cotação']
table['Preço de Venda'] = table['Preço de Compra'] * table['Margem']

# Exportar a base de dados
table.to_excel('Produtos_Atualizado.xlsx', index=False)
