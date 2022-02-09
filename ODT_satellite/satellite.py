import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

# single-ended input on channel 1
# this channel is indicator for when the pulse starts 
pulse_indicator = AnalogIn(ads, ADS.P1)




def to_velocity(speed, direction):
    retMe_x = speed * direction[0]
    retMe_y = speed * direction[1]
    retMe_z = speed * direction[2]
    return [retMe_x, retMe_y, retMe_z]
    
def list_to_string(my_list):
    x = str(my_list[0])
    y = str(my_list[1])
    z = str(my_list[2])
    retMe = x + " " + y + " " + z + "\n"
    return retMe

def to_txt(voltage, time_elapsed, number):
    my_speed = voltage * (93.25) * (0.12)
    my_range = (1.5 * (10 ** 8)) * time_elapsed
    
    direction = [0, -1, 0]
    velocity = to_velocity(my_speed, direction)
    position = [1, my_range, 0]
    
    string_velocity = list_to_string (velocity)
    string_position = list_to_string (position)
    
    with open('particle'+str(number)+'.txt', "w") as particle_file:
        particle_file.write(string_position)
        particle_file.write(string_velocity)
        
    print("success! found: '"+'particle'+str(number)+'.txt')


threshold = .5 
number = 0

while True:
    if pulse_indicator.voltage > threshold: #if it did pulse...
        print("it pulsed!")
        while pulse_indicator.voltage > threshold:
            pass
        print("receiving a pulse")
        start = time.perf_counter() # store the time of pulse
        
        while pulse_indicator.voltage < threshold:
            voltage = chan.voltage
            if voltage > threshold:
                finish = time.perf_counter()
                time_elapsed = finish - start
                to_txt(voltage, time_elapsed, number)
                number = number + 1
                break
                
                
        
        
        
            
            
            
            
            
            
            
    