import smbus  # smbus library is used 
import time  # time library is also imported here 
bus = smbus.SMBus (1) # object of smbus library is created here to access i2c based functions
def light ():
	address = bus.read_i2c_block_data (0x23, 0x23)  # here address variable will store the raw data (address) recieved in blocks recieved from sensor
	value = (address[1] + (256* address [0]))/1.2  # here raw data recieved is converted into real data (as data is stored in first two index of address,
													#                                                   so we are fetching using adress[0] and adress[1])
	return value							# value stored in variable will be returned by function light()

while(True):
	lux = light ()			# here lux is storing the value returned by light() function
	
	if (lux < 10):					# if lux is smaller than 10 then print, too dark
		print ("too dark")
	elif (lux < 50):				# if lux is smaller than 50 then print, dark
		print ("dark")
	elif (lux < 500):				# if lux is smaller than 500 then print, medium
		print ("medium")
	elif (lux > 1000):				# if lux is greater than 1000 then print, too bright
		print ("too bright")
	elif (lux < 1000):				# if lux is smaller than 1000 then print, bright
		print ("bright")
	time.sleep (1)					# used to take a delay of 1 second
