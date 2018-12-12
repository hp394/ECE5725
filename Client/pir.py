import RPi.GPIO as GPIO
import time
class pir():
	def __init__(self,pir):
		self.pir = pir
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pir, GPIO.IN)
		time.sleep(2)
		
	def detect(self):
		if GPIO.input(self.pir):
			time.sleep(1.5)
			if GPIO.input(self.pir):
				return True;
		return  False;

