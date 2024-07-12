import pyautogui;
import os
import pdfplumber

#pyautogui.hotkey('win','r')
#pyautogui.write("O CAMINHO DA FRAN")
pasta="C:\\Users\\luanp\\Documents\\ACMERobotsCerto"
lista_arquivos=os.listdir(pasta)
count=0

for arquivo in lista_arquivos:
    
    caminho_antigo=os.path.join(pasta,arquivo)
    nome, tipo=os.path.splitext(arquivo)
    nome_novo_teste=f"{count}hehe"
    caminho_novo=os.path.join(pasta, nome_novo_teste)
    os.rename(caminho_antigo,caminho_novo)
    count+=1
    


