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
import argparse

#to gb calc
gb = 10 ** 9 

user_acc = os.getlogin()

get_daydate = datetime.datetime.now()

#root directory
my_path = '/'

free_b,used_b,total_b = shutil.disk_usage(my_path)

#get capacity - free space - used space
storage_capacity_amount = free_b/gb
usedspace_amount = used_b/gb
remainingspace_amount = total_b/gb


user_platform = sys.platform

user_platform_rel = platform.release()

physicalcore_count = psutil.cpu_count(logical=False)
totalcore_count = psutil.cpu_count(logical=True)


bytes_sent = psutil.net_io_counters().bytes_sent
bytes_recv = psutil.net_io_counters().bytes_recv

per_cpu = psutil.cpu_percent(percpu=True, interval=1)

#choice for charts
chart_choice = ''

#function to get user account & time accessed
def get_account():   
    #get time accessed
    time_acc = datetime.datetime.now()
    #print username logged in
    print(f"User: {user_acc}")
    #print time accessed - now
    print(f"Last accessed: {time_acc}")      


#get platform related info 
def get_platform():
    #get the platform itself
    print(f"Platform: {user_platform}")
    #get the version release 
    print(f"Platform Release: {user_platform_rel} \n")
    #sent amount 
    print(f'Total Bytes Sent: {get_size(bytes_sent)}')
    #recieved amount 
    print(f'Total Bytes Recieved: {get_size(bytes_recv)} \n')
    print(f'Physical Core Count: {physicalcore_count}')
    print(f'Total Core Count: {totalcore_count}')
    
  
#this function  converts larger numbers into - Kilobytes - MegaBytes - Gigabytes - TeraBytes - PetaBytes
def get_size(bytes, suffix="B"):
    fact = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < fact:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= fact


# % of usage per core & total CPU usage %
def usageper_core():
    for i, percentage in enumerate(per_cpu):
      print(f'Core {i}: {percentage}%')
    print(f'Total CPU Usage: {psutil.cpu_percent()}% \n')   


#print capacity in Bytes
def get_capacity(my_path):    
    #print(f'Capacity: {:6.2f} GB \n'.format(free_b/gb))
    print('Capacity: {:6.2f} GB'.format(free_b/gb))
    

#print used space in Bytes    
def get_usedSpace(my_path):
      #print(f"Used Space: {used_b} \n")
      print('Used: {:6.2f} GB '.format(used_b/gb) )


#print remaining in Bytes
def get_TotalSpace(my_path):
    #print(f"Total Space: {total_b} \n")
    print('Remaining: {:6.2f} GB'.format(total_b/gb))


#show space in bar chart - also interactive
def graph_space():
   #give bar chart window title
   bargraphwin_title = plt.figure("Storage Bar Chart")  
   #here i have given what needs to be put in the graph, what we are graphing
   usage_types = (f'Storage Capacity \n {round(storage_capacity_amount,2)} GB', f'Used Space \n {round(usedspace_amount,2)} GB', f'Remaining Space \n {round(remainingspace_amount,2)} GB')
   #arange our space types 
   y_pos = np.arange(len(usage_types))
   #a list of our usage_points, in the list individually round them off to the 2nd decimal  
   usage_points = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)] 
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
    usage_sizes = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)]
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
   

def get_args(chart_choice):
    parser = argparse.ArgumentParser()
    parser.add_argument("--barchart", help="Type either --barchart barchart or --piechart piechart to see results visually")
    parser.add_argument("--piechart")
    args = parser.parse_args()

    if args.barchart:
       print(f'Launching {args.barchart}..')
       plt.show(graph_space())
    elif args.piechart:
        print(f'Launching {args.piechart}..')
        plt.show(gen_piGraph()) 
         
        


get_account()  
get_platform()
usageper_core()
get_capacity(my_path)
get_usedSpace(my_path)
get_TotalSpace(my_path)
get_args(chart_choice)
graph_space()
gen_piGraph()
#plt.show()
