# -*- coding: utf-8 -*-
'''
@Author: Gustavo Maciel
@Description: The code here was develop as part of Cognizant Graduation Program selection.
			  The sentences here are written in Portuguese (pt-br)

@Library used:
'''
import os
import sys
import pyttsx3

maria_voice = r'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_PT-BR_MARIA_11.0'
#Sentence's definition
notFound = 'Não foi possivel encotrar o contato, por favor, tente novamente'
askYourName = 'Por favor, diga seu nome completo:'
askEmployeeName = 'Por favor, diga o nome completo de quem você gostaria de falar:'

#Define função para facilitar a chamada
def speech(sentence):
	try:
		engine = pyttsx3.init()
		engine.setProperty('voice', maria_voice)
		print(sentence)
		engine.say(sentence)
		engine.runAndWait()

	except Exception as e:
		print('Error: ', e)