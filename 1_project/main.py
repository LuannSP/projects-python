"""
    Projeto 1:
    Passo 1 - Entrar no sistema da empresa. (entrar no link)
    Passo 2 - Navegador no sistema e encontrar a base de dados (pasta exportar)
    Passo 3 - Download da base de daddos
    Passo 4 - Calcular os indicadores (faturamento, quantidade de produtos vendidos)
    Passo 5 - Entrar no email
    Passo 6 - Mandar um email para a diretoria com os indicadores
"""
import pyautogui
import pyperclip
import pandas as pd
import time

pyautogui.PAUSE = 1

# Se o link conter caracteres especiais, usar o 'import pyperclip' para copiar e colocar o link e não escrever ele.
# pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
# pyautogui.hotkey('ctrl', 'v')
pyautogui.press('win')
pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.press('enter')

time.sleep(8)

# Fullscreen 1920:1080 -> Point(x=324, y=226) -> 'Exportar'
pyautogui.click(x=324, y=226, clicks=2)

# Baixando a base de dados
pyautogui.rightClick()

# Fullscreen 1920:1080 -> Point(x=459, y=582) -> 'Download'
pyautogui.click(x=459, y=582)

time.sleep(5)

table = pd.read_excel(r'C:\Users\luann\Downloads\Vendas - Dez.xlsx')

quantity = table['Quantidade'].sum()
invoicing = table['Valor Final'].sum()

# Acessando o gmail
pyautogui.press('win')
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('enter')

time.sleep(8)

# Mandando o email (gmail)
# Passo 1 - Clicar no botão '+'
# Passo 2 - Escrever o destinatario
# Passo 3 - Escrever o assunto
# Passo 4 - Escrever escopo do email
# Passo 5 - Enviar email

# Fullscreen 1920:1080 -> Point(x=73, y=147) -> '+'
pyautogui.click(x=73, y=147)

pyautogui.write('luann2v2v@hotmail.com')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyperclip.copy('Relatório - Vendas - Dezembro')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# Escopo do email
pyperclip.copy(f"""

Relatório:

Quantidade de vendas em dezembro: R$ {quantity:,.2f}

Faturamento de dezembro: R$ {invoicing:,.2f}

Att, Luann Alves.

""")
pyautogui.hotkey('ctrl', 'v')

time.sleep(3)

# Enviando o email
# Fullscreen 1920:1080 -> Point(x=1423, y=1052) -> 'Send'
pyautogui.click(x=1423, y=1052)
