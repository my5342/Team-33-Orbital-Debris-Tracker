direct = "C:\\Users\\Mingi\\Documents\\Tamu\\3 Junior\\2021 Fall\\ECEN 403\\DemoThis\\particle" #insert directory
init = "particle" #insert file initial
ext = ".txt" #insert file extension (.txt, .dat, etc...)

def get_x(my_list):
    i = 0
    ret_me = []
    while i < len(my_list):
        ret_me.append(my_list[i])
        i = i + 3
    return ret_me
def get_y(my_list):
    i = 1
    ret_me = []
    while i < len(my_list):
        ret_me.append(my_list[i])
        i = i + 3
    return ret_me
def get_z(my_list):
    i = 2
    ret_me = []
    while i < len(my_list):
        ret_me.append(my_list[i])
        i = i + 3
    return ret_me

def to_float(my_string):
    list1 = my_string.split(",")
    list2 = map(float, list1)
    list3 = list(list2)
    return list3

import os.path

def my_wait():
    while True:
        if os.path.exists(direct+"/"+init+str(0)+ext):
            break

import matplotlib.pyplot as plt
import matplotlib.animation as animation

my_wait()

# Set up formatting for the movie files
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=24, metadata=dict(artist='Me'), bitrate=1800)


# Insert grid limits:
xmin = -5.2
ymin = -5.2
xmax = -xmin
ymax = -ymin
zmin = -5.2
zmax = -zmin

ax = plt.axes(projection='3d')

def animate(i):
    
    with open('animator.csv', "r") as csv_file:
        line = csv_file.readline()
    while line == '':
        with open('animator.csv', "r") as csv_file:
            line = csv_file.readline()
    
    pos = to_float(line)
    x = get_x(pos)
    y = get_y(pos)
    z = get_z(pos)
    
    plt.cla()
    
    plt.title("orbital simulation", loc='center')
    
    # Setting the axes properties
    ax.set_xlim3d([xmin, xmax])
    ax.set_xlabel('x (km)')
    ax.set_ylim3d([ymin,ymax])
    ax.set_ylabel('y (km)')
    ax.set_zlim3d([zmin,zmax])
    ax.set_zlabel('z (km)')
    
    ax.plot3D(0, 0, 0, 'o', markersize=30, color='green')
    
    i = 0
    while i < len(x):
        ax.plot3D(x[i], y[i], z[i], 'o', markersize=1, color='blue')
        i = i + 1
    
    

ani = animation.FuncAnimation(plt.gcf(), animate, interval=100)

#ani.save('filename.mp4', writer=writer)
#ani.save('C:\\Users\\Mingi\\Documents\\Tamu\\3 Junior\\2021 Fall\\ECEN 403\\DemoThis', writer='Pillow', fps=10)

plt.show()