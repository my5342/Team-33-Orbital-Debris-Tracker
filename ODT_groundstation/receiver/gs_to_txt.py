import sys
from os.path import exists

# print("to_txt: '",sys.argv[1],"'")
my_str = sys.argv[1]
my_arr = my_str.split(",")
#print(type(my_str))
#print(my_arr)

#my_arr at this point should have position and velocity data
direct  = "/home/mingiyeo/Documents/ground_station/particle"
init = "particle"
ext = ".txt"
if not exists(direct+"/"+init+my_arr[0]+ext):
    with open(direct+"/"+init+my_arr[0]+ext,"w") as particle_file:
        particle_file.write(my_arr[1]+" "+my_arr[2]+" "+my_arr[3]+"\n"+my_arr[4]+" "+my_arr[5]+" "+my_arr[6]+"\n")
