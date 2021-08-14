import pyautogui   
import pyperclip
import time
from selenium import webdriver

# Passo 1 iniciar, encerrar e salvar na pasta a gravação da tela
pyautogui.click(x=856, y=188, clicks=1) #altere essa linha conforme o tamanho da sua tela (area do click "area de trabalho")
time.sleep(2)
pyautogui.write('debut video capture software')
time.sleep(6)
pyautogui.press('enter')
time.sleep(7)
pyautogui.hotkey('ctrl', 'f9')
time.sleep(10)
pyautogui.hotkey('ctrl', 'f10')
time.sleep(2)
pyautogui.click(x=932, y=101) #altere essa linha conforme o tamanho da sua tela (area do click "minimizar")
time.sleep(2)
# Passo 2 Abrir o google drive
driver = webdriver.Firefox(executable_path=r'C:\Users\Caioz\Desktop\geckdriver/geckodriver')
driver.get('http://drive.com')
# Carregar o arquivo
# Salve o arquivo 
# Desligue o computador
