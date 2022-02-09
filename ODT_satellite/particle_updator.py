import math
import time
import os.path

direct = "C:\\Users\\Mingi\\Documents\\Tamu\\3 Junior\\2021 Fall\\ECEN 403\\DemoThis\\particle" #insert directory
init = "particle" #insert file initial
ext = ".txt" #insert file extension (.txt, .dat, etc...)


def matrix_multiplication_3x3_3x1(A, B):
    top = A[0][0]*B[0] + A[1][0]*B[1] + A[2][0]*B[2]
    middle = A[0][1]*B[0] + A[1][1]*B[1] + A[2][1]*B[2]
    bottom = A[0][2]*B[0] + A[1][2]*B[1] + A[2][2]*B[2]
    return [top, middle, bottom]

def unit_vector(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    magnitude = (float(x))**2 + (float(y))**2 + (float(z))**2
    new_x = x/math.sqrt(magnitude)
    new_y = y/math.sqrt(magnitude)
    new_z = z/math.sqrt(magnitude)
    return [new_x, new_y, new_z]

def r_to_a(r_point, transformation):
    a_point = matrix_multiplication_3x3_3x1(transformation, r_point)
    return a_point    

# [TODO] now worry about the 2D portion
def speed(v):
    retMe = (float(v[0]))**2 + (float(v[1]))**2 + (float(v[2]))**2
    return math.sqrt(retMe)

def radius(p):
    retMe = (float(p[0]))**2 + (float(p[1]))**2 + (float(p[2]))**2
    return math.sqrt(retMe)

def circumference(radius):
    retMe = 2 * math.pi * radius
    return float(retMe)

def pretty_printer(my_list):
    i = 0
    retMe = ""
    while i < len(my_list):
        retMe = retMe + str(my_list[i]) + " "
        i = i + 1
    retMe = retMe[:-1]
    retMe = retMe + "\n"
    return retMe

def string_to_list(my_str):
    a = my_str.split()
    b = map(float, a)
    c = list(b)
    return c

def list_to_string(my_list):
    retMe = ""
    i = 0
    while i < len(my_list):
        retMe = retMe + str(my_list[i]) + " "
        i = i + 1
    retMe = retMe[:-1]
    retMe = retMe + "\n"
    return retMe

def update_particle(number):
    #find the current position
    with open(direct+"/"+init+str(number)+ext, "r") as particle_file:
        lines = particle_file.readlines()
    while lines == []:
        with open(direct+"/"+init+str(number)+ext, "r") as particle_file:
            lines = particle_file.readlines()
        
    position = string_to_list(lines[0])
    velocity = string_to_list(lines[1])
    
    #transformation (ie rotation)
    i = unit_vector(position)
    j = unit_vector(velocity)
    k = [0.0, 0.0, 1.0]
    
    transformation = [i, j, k]
    
    #where is the particle?
    s = speed(velocity)
    r = radius(position)
    arc_length = s * .1
    theta = arc_length/r
    r_p_x = r * math.cos(theta)
    r_p_y = r * math.sin(theta)
    
    r_v_x = s * math.cos(theta+math.pi/2)
    r_v_y = s * math.sin(theta+math.pi/2)
    
    new_position = r_to_a([r_p_x, r_p_y, 0], transformation)
    new_velocity = r_to_a([r_v_x, r_v_y, 0], transformation)
    
    with open(direct+"/"+init+str(number)+ext, "w") as particle_file:
        particle_file.write(list_to_string(new_position))
        particle_file.write(list_to_string(new_velocity))
    
    
while True:
    i = 0
    while os.path.exists(direct+"/"+init+str(i)+ext):
        update_particle(i)
        i = i + 1
    time.sleep(.1)




















