import serial
import time
import sys


if __name__ == '__main__':
    send_me = sys.argv[1]
    send_me += "\n"
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    
    ser.write(bytes(send_me, 'utf-8'))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)
