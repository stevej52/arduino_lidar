import time
import digitalio
import board
import busio
import adafruit_vl53l0x


xs1 = digitalio.DigitalInOut(board.D2)
xs1.direction = digitalio.Direction.OUTPUT
xs2 = digitalio.DigitalInOut(board.D3)
xs2.direction = digitalio.Direction.OUTPUT
xs3 = digitalio.DigitalInOut(board.D4)
xs3.direction = digitalio.Direction.OUTPUT



xs1.value = False
xs2.value = False
xs3.value = False
uart = busio.UART(board.TX1, board.RX1, baudrate=115200)

print("Starting...")
i2c = busio.I2C(board.SCL, board.SDA)

xs1.value = True
time.sleep(0.1)

print("Write 1...")
i2c.try_lock()
i2c.writeto(0x29, bytes([0x8A, 0x2A]), stop=False)
time.sleep(0.1)

print("Write 2...")
xs2.value = True
time.sleep(0.1)

i2c.unlock()

i2c.try_lock()

i2c.writeto(0x29, bytes([0x8A, 0x2B]), stop=False)
time.sleep(0.1)
i2c.unlock()
print("Write 3...")
time.sleep(0.1)

xs3.value = True
time.sleep(0.1)
i2c.try_lock()
i2c.writeto(0x29, bytes([0x8A, 0x2C]), stop=False)
time.sleep(0.1)
i2c.unlock()

xs1.value = True
xs2.value = True
xs3.value = True

i2c.try_lock()
i2c.scan()
i2c.unlock()

vl531 = adafruit_vl53l0x.VL53L0X(i2c=i2c,address=0x2A, io_timeout_s=0)
vl532 = adafruit_vl53l0x.VL53L0X(i2c=i2c,address=0x2B, io_timeout_s=0)
vl533 = adafruit_vl53l0x.VL53L0X(i2c=i2c,address=0x2C, io_timeout_s=0)

r1=str(vl531.range)
r2=str(vl532.range)
r3=str(vl533.range)


while True:

    r1=str(vl531.range)
    r2=str(vl532.range)
    r3=str(vl533.range)
    rz1="{:0>4}".format(r1)
    rz2="{:0>4}".format(r2)
    rz3="{:0>4}".format(r3)

    distance_string = ":"+rz1+":"+str(rz2)+":"+str(rz3)+":"


    print(distance_string)
    encode_string = distance_string.encode('utf-8')
    uart.write(encode_string)

    time.sleep(.04)
xs1.value = False
xs2.value = False
xs3.value = False
vl531.deinit()
vl532.deinit()
vl533.deinit()
i2c.deinit()
