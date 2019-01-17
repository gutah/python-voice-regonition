'''
@Author: Gustavo Maciel
@Description: The code here was develop as part of Cognizant Graduation Program selection.
			  The sentences here are written in Portuguese (pt-br)

@Library used:
'''
from translate import Translator
from speak import speech
import speech_recognition as sr
import time
import nltk

def translate(text):
	translator= Translator(from_lang="portuguese",to_lang="english")
	translation = translator.translate(text)
	return translation

def interpreting(text):
	try:
		#clean variables
		person_list = []
		person = []
		name = ""		
		
		t_text = translate(text)#Translate the text from Portuguese to English, for a more accurate understanding
		frase = nltk.tokenize.sent_tokenize(t_text)
		tokens = nltk.word_tokenize(t_text)#Sentence tolkenize
		classes = nltk.tag.pos_tag(tokens)#Classify the words
		entidades = nltk.chunk.ne_chunk(classes)#Categorize the words
		
		#Logic to extrat only the names from the spoken sentence
		for subtree in entidades.subtrees(filter=lambda t: t.label() == 'PERSON' or t.label()=='GPE'):
		    for leaf in subtree.leaves():
		        person.append(leaf[0])
		    if len(person) > 0:
		        for part in person:
		            name += part + ' '
		        if name[:-1] not in person_list:
		            person_list.append(name[:-1])
		        name = ''
		    person = []
		qtde_itens_na_lista = len(person_list)

		#if more then one object 
		if(qtde_itens_na_lista>1):
			#Board objects
			name = ' '.join(person_list)
			return name
		
		#if only one object at list
		if(qtde_itens_na_lista == 1):
			#convert List to String
			strName = ' '.join(person_list)
			#Divides the converted String
			name = strName.split(' ')
			#Valid if the new list has more than one object
			if(len(name)<2):
				return 0
			return strName
		return 0	
	except Exception as e:
		print ('An error occurred: ', e)
		return 0

def listening(text):
	texto = text
	r = sr.Recognizer()
	with sr.Microphone() as source:#Starts Microfone
	    r.adjust_for_ambient_noise(source, duration=3)#Ajust background noise
	    i = 0
	    while (i!=3):
	        try:
	            name='' #clean variable
	            speaks(texto) 
	            audio = r.listen(source, phrase_time_limit=5)#Capture audio
	            audio_ouvido = r.recognize_google(audio, language="pt-BR")#Call Google API
	            print('Interpretando.')
	            name = interpreting(audio_ouvido)#Interprets the text understood by the API
	            print('Finalizado')
	            #Validate if error equal to zero is error
	            if(name != 0):
		            return name
	        except:
	            if(i == 2):
	                speaks('Número de tentativas excedidas, digite por favor.')
	                name = input()
	                return name
	            else:
	                speaks("Não entendi o que disse.")
	                i+= 1