import serial
import time

ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)

strip1="0000"

x=0

while True:
	x=x+1

	ser1_rl=ser1.readline()
	strip1=str(ser1_rl.rstrip().decode('utf-8'))
	rstrip=strip1[2:6]
	fstrip=strip1[10:14]
	lstrip=strip1[18:22]
	rn=int(rstrip)
	fn=int(fstrip)
	ln=int(lstrip)
	print(strip1)

#	print(lstrip)




