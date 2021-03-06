#!/usr/bin/python
# -*- coding: utf-8 -*-
print '\033[36m'+'   _____       _   _               '+'\033[0;0m'
print '\033[36m'+' _|  __ \     | | | |              '+'\033[0;0m'
print '\033[36m'+'(_) |  \/ __ _| |_| |__   ___ ____ '+'\033[0;0m'
print '\033[36m'+'| | | __ / _` | __|  _ \ / _ \  __|'+'\033[0;0m'
print '\033[36m'+'| | | |_\ \ (_| |_| | | | |__/ |   '+'\033[0;0m'
print '\033[36m'+'|_|\____/\__,_|\__|_| |_|\___|_|   '+'\033[0;0m'
print ' '
print '\033[35m'+' ######################### '+'\033[0;0m'
print '\033[35m'+' # Information Gathering # '+'\033[0;0m'
print '\033[35m'+' # ----------//--------- # '+'\033[0;0m'
print '\033[35m'+' # By: Scatolin          # '+'\033[0;0m'
print '\033[35m'+' ######################### '+'\033[0;0m'
print ' '

#Importando bibliotecas
import socket,sys,subprocess,requests
from datetime import datetime

#Checando o horario em que o scan inicia
t1 = datetime.now()
print '\033[31m'+'[*] Recon iniciado em: ',t1
print ' '+'\033[0;0m'

#Menu de seleção de recursos
opcao = 0
while opcao != 5:
	print ' ___________________________'
	print '|                           |'
	print '| \033[32m'+'[1] '+'\033[0;0m''Resolver host         |'
	print '| \033[32m'+'[2] '+'\033[0;0m''Varrer Portas         |'
	print '| \033[32m'+'[3] '+'\033[0;0m''Escanear Diretórios   |'
	print '| \033[32m'+'[4] '+'\033[0;0m''Escanear Subdomínios  |'
	print '|___________________________|'
	print ' '
	opcao = int(input('=> Selecione a ferramenta desejada:'))

#Resolvendo host
	if opcao == 1:
		print '*Ex: alvo.com*'
		resolve = raw_input('=> Insira a URL alvo: ')
		print ''
		print '[*] Resolvendo URL...'
		print '\033[32m'+'[+] '+'\033[0;0m STATUS ==> Online'
		print '\033[32m'+'[+] '+'\033[0;0m URL    ==>', resolve 
		print '\033[32m'+'[+] '+'\033[0;0m', "IP     ==>",socket.gethostbyname(resolve);

#Escaneando portas
	elif opcao == 2:
		print ' '
		portas = [21, 22, 23, 25, 53, 66, 79, 80, 107, 110, 111, 118, 119, 137, 138, 139, 143, 150, 161, 194, 209, 217, 389, 407, 443, 445, 465, 515, 522, 531, 568, 569, 587, 666, 700, 701, 992, 993, 995, 1024, 1414, 1417, 1418, 1419, 1420, 1424, 1434, 1503, 1547, 1720, 1731, 1812, 1813, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2400, 2611, 2612, 3000, 3128, 3306, 3389, 3568, 3569, 4000, 4099, 4661, 4662, 4665, 5190, 5500, 5631, 5632, 5670, 5800, 5900, 6003, 6112, 6257, 6346, 6500, 6667, 6699, 6700, 6880, 6891, 6892, 6893, 6894, 6895, 6896, 6897, 6898, 6899, 6900, 6901, 7000, 7002, 7013, 7500, 7640, 7642, 7648, 7649, 7777, 7778, 7779, 7780, 7781, 8000, 8080, 9000, 9004, 9005, 9008, 9012, 9013, 12000, 12053, 12083, 12080, 12120, 12122, 24150, 26000, 26214, 27015, 27500, 27660, 27661, 27662, 27900, 27910, 47624, 56800]
		print '*Ex: 127.0.0.1*'
		ip = raw_input("=> Insira o IP para o PortScan: ")
		print ' '
		print '[*] Escaneando portas...'

		for porta in portas:
			cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			cliente.settimeout(0.5)
			codigo = cliente.connect_ex((ip, porta))
			if codigo == 0:
				print '\033[32m'+'[+] '+'\033[0;0m' "Porta:" , porta, "==> Aberta!"

	# Escaneando e retornando diretorios encontrados
	elif opcao == 3:
		print ' '
		print '*Ex: https://alvo.com/*'
		url = raw_input('Insira a URL para o scan de diretorios: ')
		print '*Ex: /wordlist/common.txt*'
		print '* Escolha a Wordlist compatível com sua necessidade! *'
		wordlist = raw_input('Insira o caminho para a Wordlist: ')
		print ' '
		print '[*] Varrendo diretorios...'
		def write(word):
			f1 = open(".txt","a")
			f1.write(word +"\n")

		fo = open(wordlist, "r+")
		for i in range(1000): #Varrendo 1000 diretorios, editar o numero para adaptar a wordlist
			word = fo.readline(10).strip()
			surl = url+word

			response = requests.get(surl)
			if (url != surl) and (response.status_code == 200):
				print '\033[32m'+'[+]'+'\033[0;0m' "200 OK ==>",surl
				write(word)
				pass

#Escaneando subdomínios
#elif opcao == 4:
else:
	print '\033[31m'+'[*]'''+'\033[0;0m'' Opção inválida! Tente novamente.'
print '\033[31m'+'[*]'''+'\033[0;0m'' Operação cancelada pelo usuário.'

# Checando o horario em que o scan termina
t2 = datetime.now()

# Calculando o tempo que foi gasto durante a execucao
total = t2 - t1

# Exibindo os valores de tempo
print ' '
print '\033[31m'+'[*] Recon terminado em: ',t2
print 'Tempo gasto: ', total
print ' '+'\033[0;0m'