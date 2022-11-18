import smbus
import time
bus = smbus.SMBus (1)
def light ():
	address = bus.read_i2c_block_data (0x23, 0x23)
	value = (address[1] + (256* address [0]))/1.2
	return value
while(True):
	lux = light ()
	#print (lux)
	if (lux < 10):
		print ("too dark")
	elif (lux < 50):
		print ("dark")
	elif (lux < 500):
		print ("medium")
	elif (lux > 1000):
		print ("too bright")
	elif (lux < 1000):
		print ("bright")
	time.sleep (1)