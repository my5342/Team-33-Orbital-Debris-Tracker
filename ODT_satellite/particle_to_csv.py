import os.path
import time


direct = "C:\\Users\\Mingi\\Documents\\Tamu\\3 Junior\\2021 Fall\\ECEN 403\\DemoThis\\particle" #insert directory
init = "particle" #insert file initial
ext = ".txt" #insert file extension (.txt, .dat, etc...)

def my_wait():
    while True:
        if os.path.exists(direct+"/"+init+str(0)+ext):
            break

def particle_count():
    retMe = []
    i = 0
    while os.path.exists(direct+"/"+init+str(i)+ext):
        retMe.append(i)
        i = i + 1
    return retMe

def get_position(number):
    with open(direct+"/"+init+str(number)+ext, "r") as csv_file:
        lines = csv_file.readlines()
    while lines == []:
        with open(direct+"/"+init+str(number)+ext, "r") as csv_file:
            lines = csv_file.readlines()
    position = lines[0]
        
    return position

def to_csv(given):
    my_string = ""
    for i,line in enumerate(given):
        my_string = my_string + str(line.split()[0]) + "," + str(line.split()[1]) + "," + str(line.split()[2]) + ","
    my_string = my_string[:-1]
    my_string = my_string + "\n"
    with open('animator.csv', "w") as csv_file:
        csv_file.write(my_string)

my_wait()

while True:
    particleList = particle_count()
    results1 = map(get_position, particleList)
    results2 = list(results1)
    to_csv(results2)
    time.sleep(.1)