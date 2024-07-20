import pyautogui
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Função para encontrar botão por XPath
def encontrar_botao(navegador, xpath):
    WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    botao = navegador.find_element(By.XPATH, xpath)
    return botao

caminho_pasta = "********************"
lista_arquivos = os.listdir(caminho_pasta)

# Configuração do navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)
navegador.maximize_window()

def acesso_tasy():
    try:
        lista_nome, lista_caminhos_antigos = pegar_nomes_arquivos()
        count = 0
        
        navegador.get('https://**************/#/login')  
        sleep(5)
       
        # Realizar login
        encontrar_botao(navegador, '//*[@id="loginUsername"]').send_keys('*********')
        encontrar_botao(navegador, '//*[@id="loginPassword"]').send_keys('*******')
        encontrar_botao(navegador, '//*[@id="loginForm"]/input[3]').click()
        
        # Botão OK para trocar de estabelecimento
        encontrar_botao(navegador, '//*[@id="ngdialog1"]/div[2]/div[1]/div[2]/button[1]').click()
        
        # Fechar comunicação interna
        encontrar_botao(navegador, '//*[@id="header"]/div[1]/div/button').click()
        
        sleep(2)
        print(pyautogui.position())
        xx, yy = pyautogui.position()
        pyautogui.click(xx, yy)
        
        sleep(2)
        # Barra de pesquisa
        encontrar_botao(navegador, '//*[@id="app-view"]/tasy-corsisf1/div/w-mainlayout/div/div/w-launcher/div/input').send_keys('Prontuário Eletrônico Pacient')
        
        sleep(2)
        # Botão para abrir prontuário eletrônico
        encontrar_botao(navegador, '//*[@id="app-view"]/tasy-corsisf1/div/w-mainlayout/div/div/w-launcher/div/div/div[1]/w-apps/div/div[1]/ul/li/w-feature-app/a/span').click()
        
        sleep(15)
        pyautogui.click(152, 188)
        
        sleep(9)
        pyautogui.write(f"{lista_nome[count]}")
        sleep(2)
        pyautogui.press('enter')
        
        sleep(2)
        # Botão OK após selecionar prontuário
        encontrar_botao(navegador, '//*[@id="handlebar-452235"]').click()
        
        # Botão fechar após selecionar prontuário
        encontrar_botao(navegador, '//*[@id="handlebar-673782"]').click()
        
        # Botão GED
        encontrar_botao(navegador, '//*[@id="title_4_11_10"]').click()
        
        sleep(3)
        pyautogui.click(1329, 27)
        
        # Botão para documentos
        encontrar_botao(navegador, '//*[@id="layout"]/div/div/tasypopupmenu/tasy-wdbpanel/div/div[2]/div[5]/div[1]/w-datagrid/div[1]/span/div/button').click()
        
        sleep(6)
        pyautogui.click(1221, 449)
        pyautogui.scroll(-100)
        
        # Botão para selecionar arquivo
        encontrar_botao(navegador, '//*[@id="btnDS_ARQUIVO"]').click()
        
        sleep(4)
        pyautogui.write(f"{lista_caminhos_antigos[count]}")
        sleep(5)
        pyautogui.press("enter")
        sleep(6)
        pyautogui.click(1286, 629)
        sleep(5)
        
        # Botão para liberar documento
        encontrar_botao(navegador, '//*[@id="layout"]/div/div/tasypopupmenu/tasy-wdbpanel/div/div[2]/div[2]/button').click()
        
        sleep(5)
        pyautogui.press("enter")
        sleep(5)
        
        for arquivo in lista_arquivos:
            count = count + 1
            
            sleep(4)
            print(pyautogui.position())
            x, y = pyautogui.position()
            pyautogui.click(372, 199)
            print(x, y)
            sleep(2)
            
            pyautogui.write(f"{lista_nome[count]}")
            pyautogui.press('enter')
            sleep(8)
            
            # Botão fechar após selecionar prontuário
            encontrar_botao(navegador, '//*[@id="handlebar-673782"]').click()
            
            # Botão GED
            encontrar_botao(navegador, '//*[@id="title_4_11_10"]').click()
            
            sleep(3)
            pyautogui.click(1329, 27)
            
            # Botão para documentos
            encontrar_botao(navegador, '//*[@id="layout"]/div/div/tasypopupmenu/tasy-wdbpanel/div/div[2]/div[5]/div[1]/w-datagrid/div[1]/span/div/button').click()
            
            sleep(6)
            pyautogui.click(1221, 449)
            pyautogui.scroll(-100)
            
            # Botão para selecionar arquivo
            encontrar_botao(navegador, '//*[@id="btnDS_ARQUIVO"]').click()
            
            sleep(4)
            pyautogui.write(f"{lista_caminhos_antigos[count]}")
            sleep(6)
            pyautogui.press("enter")
            sleep(3)
            pyautogui.click(1286, 629)
            sleep(5)
            
            # Botão para liberar documento
            encontrar_botao(navegador, '//*[@id="layout"]/div/div/tasypopupmenu/tasy-wdbpanel/div/div[2]/div[2]/button').click()
            
            sleep(5)
            pyautogui.press("enter")
            sleep(5)
            
            nome_novo = f"{lista_nome[count]}PRONTO"
            caminho_novo = os.path.join(caminho_pasta, nome_novo)
            os.rename(lista_caminhos_antigos[count], caminho_novo)
            sleep(5)
            
        sleep(5)
    except Exception as e:
        print(f'Erro: {e}')
        sleep(3)

def pegar_nomes_arquivos():
    lista_nome = []
    lista_caminho_antigo = []
    for arquivo in lista_arquivos:
        caminho = os.path.join(caminho_pasta, arquivo)
        lista_caminho_antigo.append(caminho)
        nome, tipo = os.path.splitext(arquivo)
        lista_nome.append(nome)
    return lista_nome, lista_caminho_antigo

lista_nome, lista_caminhos_antigos = pegar_nomes_arquivos()

acesso_tasy()
