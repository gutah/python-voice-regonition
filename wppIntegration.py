'''
@Author: Gustavo Maciel
@Description: The code here was develop as part of Cognizant Graduation Program selection.
			  The sentences here are written in Portuguese (pt-br)

@Library used:
    To run this code you need to install selenium library amd intall chromedriver extension

    To install selenium:
        - in python shell run the comand: pip install selenium
    To install chormedrive:
        - Download the chorme extension at: http://chromedriver.chromium.org/downloads
        - Is recomended that you save the extensio at 'C:/drive/chromedriver.exe'
          if you save copy and past the new path at 'drive' variable
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from speak import speak

'''
googleChromeProfile this variable is response to sabe the user profile, so you 
whatsApp won't ask to login more then once
'''
googleChromeProfile = r'user-data-dir=C:/Users/Graduation19/AppData/Local/Google/Chrome/User Data --profile-directory=Profile 1'
drive = r'C:/drive/chromedriver.exe'


def sendMessage(requester, contact):
    SolicitanteStr = requester #message you want to send
    ContatoStr = contact #contact to be search
    options = webdriver.ChromeOptions() 
    options.add_argument(googleChromeProfile) #Path to Google Chrome user profile
    chromedriver = webdriver.Chrome(chrome_options=options, executable_path=drive) #Chrome driver path 

    print('Conectando no WhatsApp')
    chromedriver.get(('http://web.whatsapp.com'))#website link
    time.sleep(5) #wait website be load

    i = 0
    while(True):

        try:
            time.sleep(10) #wait website be load
            novac = chromedriver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div')
            if novac.is_enabled():
                novac.click()
                chromedriver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input').click() #clica no campo Pesquisa de contatos do zap
                contato = chromedriver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input') #seleciona o campo de pesquisa de contatos do zap para que possa enviar o texto
                contato.send_keys(ContatoStr) #input the name at the field
                time.sleep(2) #wait to load the contact search bar
                try:
                    elem = chromedriver.find_element_by_css_selector('div._1vDUw._2sNbV')
                    if elem.is_enabled():
                        chromedriver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input').send_keys(Keys.ENTER)#pressiona enter para abrir conversa
                        time.sleep(2) #wait for the conversation to load
                        solicitante = chromedriver.find_element_by_css_selector('div._2S1VP.copyable-text.selectable-text')#seleciona o campo de texto para enviar a mensagem
                        solicitante.send_keys("Olá, " + SolicitanteStr + " está te aguardando na recepção"+ Keys.ENTER)#Digita a mensagem para o contato e envia
                        return 1
                except:
                    speak("Desculpe, não foi possível encontrar o colaborador informado, por favor, dirija-se a recepção.")
            
        except:
            if(i!=3):
                print("Erro ao conectar")
                chromedriver.refresh()
                i += 1
            else:

                break        