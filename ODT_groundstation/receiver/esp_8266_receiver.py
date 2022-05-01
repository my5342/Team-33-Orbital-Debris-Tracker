import serial
import subprocess

# read Serial.println
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.reset_input_buffer()
    
    particle_number = 0
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            line = str(particle_number)+","+line
            print("Received: "+line)
            subprocess.Popen(["python","gs_to_txt.py",line])
            particle_number = particle_number+1
            #subprocess.Popen(["python","satellite_to_csv.py",line])
