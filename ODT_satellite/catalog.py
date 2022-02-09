direct = "C:\\Users\\Mingi\\Documents\\Tamu\\3 Junior\\2021 Fall\\ECEN 403\\DemoThis\\particle" #insert directory
init = "particle" #insert file initial
ext = ".txt" #insert file extension (.txt, .dat, etc...)


import os.path

def string_to_list(my_str):
    a = my_str.split()
    b = map(float, a)
    c = list(b)
    return c

user_input = input("Enter particle number ('q' to quit): ")

while user_input != 'q':
    if os.path.exists(direct+"/"+init+user_input+ext):    
        with open(direct+"/"+init+str(user_input)+ext, "r") as particle_file:
            particle_info = particle_file.readlines()
        position = string_to_list(particle_info[0])
        velocity = string_to_list(particle_info[1])
        print("position: ", position)
        print("velocity: ", velocity)
    else:
        print("'"+init+user_input+ext+"'"+" does not exist!")
    user_input = input("Enter particle number ('q' to quit): ")

print("End of program!")