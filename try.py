import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyUSB0')
# board = pyfirmata.Arduino('/dev/ttyACM0')


x = int(input("enter one or zero  "))
print(time.)
if x==1:
   board.digital[13].write(1)

else:
    board.digital[13].write(0)
































