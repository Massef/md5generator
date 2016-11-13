''' Not finish'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
import crypt
import hashlib


Dict = open('dico/rockyou.txt' , 'r')

for word in Dict.readlines():
	word = word.strip('\n')
	m = hashlib.md5()
	m.update(word)	
	#c= m.hexdigest()	
	result= open('dico/result.txt', 'a') # Ouvrir un fichier en ecriture
	result.write(m.hexdigest() + '\n')	     # ecrire les md5 hash
	Dict.close()
	result.close()			     # ferme le fichier
						
