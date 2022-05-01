#this is helper code to call transmitter
import subprocess

while True:
    #read the csv file until a data pops up
    with open('particle_data_to_send.csv', "r") as csv_file:
        line = csv_file.read()
    while (line == ''):
        with open('particle_data_to_send.csv', "r") as csv_file:
            line = csv_file.read()

    #remove the first line of the csv_file
    line = line.split("\n")
    line = line[:-1]

    with open('particle_data_to_send.csv', "w") as csv_file:
        csv_file.write('')

    with open('particle_data_to_send.csv', "a") as csv_file:
        for write_me in line[1:]:
            csv_file.write(write_me + '\n')
    
    subprocess.call(["python","esp_8266_transmitter.py",line[0]])
