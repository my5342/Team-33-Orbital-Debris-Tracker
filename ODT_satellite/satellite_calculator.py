#import for radar module to data
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
#---------------------------------------------------
#import for data to tranmitter
import struct
#---------------------------------------------------
#import for tranmitter
import subprocess
#---------------------------------------------------

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
freq_to_voltage = AnalogIn(ads, ADS.P0)
# single-ended input on channel 1
# this channel is indicator for when the pulse starts 
pulse_indicator = AnalogIn(ads, ADS.P1)


def to_velocity(speed, direction):
    retMe_x = speed * direction[0]
    retMe_y = speed * direction[1]
    retMe_z = speed * direction[2]
    return str(retMe_x) + ' ' + str(retMe_y) + ' ' + str(retMe_z)

def transmit_code(code):
    for i in range(5):
        subprocess.call(["python","satellite_transmitter.py",code])

def data_to_string(voltage, time_elapsed, number):
    #parameters
    my_speed = voltage * (93.25) * (0.12)
    my_range = (1.5 * (10 ** 8)) * time_elapsed
    direction = [0, -1, 0]
    
    #velocity bit string representation
    velocity = to_velocity(my_speed, direction)
    
    #position #bit string representation
    position = str(1) + ' ' + str(my_range) + ' ' + str(0)
    
    transmit_me = str(number) + ' ' + position + ' ' + velocity
    transmit_code(transmit_me)
    
    
threshold = .5 
number = 0

while True:
    if pulse_indicator.voltage > threshold: #if it did pulse...
        print("it pulsed!")
        start = time.perf_counter() # store the time of pulse
        while pulse_indicator.voltage > threshold:
            pass
        print("receiving a pulse")
        
        while pulse_indicator.voltage < threshold:
            voltage = freq_to_voltage.voltage
            if voltage > threshold:
                finish = time.perf_counter()
                time_elapsed = finish - start
                data_to_string(voltage, time_elapsed, number)
                number = number + 1
                break
                
                
        
        
        
            
            
            
            
            
            
            
    

