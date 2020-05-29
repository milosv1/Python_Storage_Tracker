#first imported items
import os #operating system
import sys #system
import datetime #get date and time
import shutil #allows us to work with files 
import matplotlib.pyplot as plt; plt.rcdefaults() #allows us to implement graphs and charts
import numpy as np #numpy- allows us to work with maths
import mplcursors # this is a new import allows us to interact with bar chart 
from os import path
import platform #get platform info of user
import psutil

gb = 10 ** 9 

#get users account username 
user_acc = os.getlogin()

#get time & date
get_daydate = datetime.datetime.now()

#path needed - global - '/' root directory
my_path = '/'

free_b,used_b,total_b = shutil.disk_usage(my_path)

#calculations total = total_b/gb
#Used = used_b / gb
#free = free_b / gb
#here we get the free amount, used amount and also the remaining
free_amount = free_b/gb
used_amount = used_b/gb
remaining_amount = total_b/gb

#get user platform info
user_platform = sys.platform
#show platform release
user_platformRel = platform.release()

#simply show core count of device
core_Count = os.cpu_count()

#virtual_memoryPercentage = psutil.virtual_memory()[2]/2.**30
#print('Virtual Memory: {:6.2f}'.format(virtual_memoryPercentage/2.**30))

print(" ")

#get platform related info here
def get_platform():
    #get the platform itself
    print(f"Platform: {user_platform}")
    #get the version release 
    print(f"Platform Release: {user_platformRel}")
    #show how many cores are available 
    print(f'CPU Count: {core_Count}')

#function to get user account & time accessed
def get_account():   
    #get time accessed
    time_acc = datetime.datetime.now()
    #print username logged in
    print(f"User: {user_acc}")
    #print time accessed - now
    print(f"Last accessed: {time_acc} \n")      

#print capacity in Bytes
def get_capacity(my_path):    
    #print(f'Capacity: {:6.2f} GB \n'.format(free_b/gb))
    print('{:6.2f} GB Capacity'.format(free_b/gb))
    
#print used space in Bytes    
def get_usedSpace(my_path):
      #print(f"Used Space: {used_b} \n")
      print('{:6.2f} GB Used'.format(used_b/gb) )

#print remaining in Bytes
def get_TotalSpace(my_path):
    #print(f"Total Space: {total_b} \n")
    print('{:6.2f} GB Remaining'.format(total_b/gb))

#show space in bar chart - also interactive
def graph_space():
   #give bar chart window title
   barGraphwin_Title = plt.figure("Storage Bar Chart")  
   #here i have given what needs to be put in the graph, what we are graphing
   usage_types = ('Storage Capacity', 'Used Space', 'Remaining Space')
   #arange our space types 
   y_pos = np.arange(len(usage_types))
   #a list of our usage_points, in the list individually round them off to the 2nd decimal  
   usage_points = [round(free_amount,2), round(used_amount,2), round(remaining_amount,2)] 

   #How we want our bar chart to look
   plt.bar(y_pos, usage_points, align='center', alpha=0.5)
   plt.xticks(y_pos, usage_types)
   #this title appears on the left hand side of our graph, showing exactly what we are trying to graph
   plt.ylabel('Usage Amount')
   #the title of our graph
   plt.title(f"Storage Overview for {user_acc} {get_daydate}")
   #this will allow us to interact with our graph, if you hover over a bar in the graph - it will show a value
   mplcursors.cursor()
  
   

#generate our piechart - the pie chart is generated once the bar graph is closed - FIXED
def gen_piGraph():
    # usage_labels is what parts of the pie chart will be called
    usage_labels = 'Storage Capacity', 'Used Space', 'Remaining Space'
    #the usage sizes should be rounded to 2 decimal points - this does not work %100 right now
    usage_sizes = [round(free_amount,2), round(used_amount,2), round(remaining_amount,2)]
    #we will need this to show our plot - also give window title for pie chart
    fig1, ax1 = plt.subplots(num="Storage Pie Chart")
    #Give Pie Chart title
    plt.title(f"Storage Overview for {user_acc} {get_daydate}")
    #Explode Remaining Space section of Pie Graph
    explode = (0,0,0.2)
    #what piechart will feature
    ax1.pie(usage_sizes, labels=usage_labels, autopct='%1.1f%%',shadow=True, startangle=90, explode=explode)
    #ensure that our graph is drawn as circle
    ax1.axis('equal')  
    mplcursors.cursor()
    print(" ")



get_platform()
get_account()   
get_capacity(my_path)
get_usedSpace(my_path)
get_TotalSpace(my_path)
graph_space()
gen_piGraph()
plt.show()
