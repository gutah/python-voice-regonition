# -*- coding: utf-8 -*-
'''
@Author: Gustavo Maciel
@Description: The code here was develop as part of Cognizant Graduation Program selection.
			  The sentences here are written in Portuguese (pt-br)

@Library used:
'''

from voiceRecognition import listening
from wppIntegration import sendMessage
from speak import speech

try:
	speech('Olá! Seja bem-vindo a Cognizant.')
	speech('Por favor, aguarde um momento...')

	requester = listening(sayYourName)
	contact = listening(sayEmployeeName)

	print('Solicitante: ', requester)
	print('Chamando: ', contact)

	response = sendMessage(solicitante, contact)
	if(response != 0):
		msg = 'Mensagem enviada para ' + contact + ', por favor aguarde.'
		speech(msg)
	else:
		speech('Falha no envio da mensagem, por favor, dirija-se a recepção')

except Exception as e:
	raise e
