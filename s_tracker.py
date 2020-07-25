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
from notifypy import Notify
from pathlib import Path

#to gb calc
gb = 10 ** 9
#print("GB VALUE:",gb) 

user_acc = os.getlogin()

get_daydate = datetime.datetime.now()

system_name = platform.node()

#root directory
my_path = '/'

free_b,used_b,total_b = shutil.disk_usage(my_path)

#get capacity - free space - used space
storage_capacity_amount = free_b/gb
usedspace_amount = used_b/gb
remainingspace_amount = total_b/gb

#10gb = 10,737,418,240
minspace_amount = 1024**3*10  
min_gb_value = minspace_amount/gb
#print(round(min_gb_value,2))

user_platform = sys.platform

user_platform_rel = platform.release()

physicalcore_count = psutil.cpu_count(logical=False)
totalcore_count = psutil.cpu_count(logical=True)

bytes_sent = psutil.net_io_counters().bytes_sent
bytes_recv = psutil.net_io_counters().bytes_recv

per_cpu = psutil.cpu_percent(percpu=True, interval=1)

chart_choice = ''

#function to get user account & time accessed
def get_account():   
    time_acc = datetime.datetime.now()
    print(f"User: {user_acc}")
    print(f"Last accessed: {time_acc}")      


#get platform related info 
def get_platform():
    print(f"System Name: {system_name}")
    print(f"Platform: {user_platform}")
    print(f"Platform Release: {user_platform_rel} \n")
    print(f'Total Bytes Sent: {get_size(bytes_sent)}')
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
   bargraphwin_title = plt.figure("Storage Bar Chart")  
   #here i have given what needs to be put in the graph, what we are graphing
   usage_types = (f'Storage Capacity \n {round(storage_capacity_amount,2)} GB', f'Used Space \n {round(usedspace_amount,2)} GB', f'Remaining Space \n {round(remainingspace_amount,2)} GB')
   #arange our space types 
   y_pos = np.arange(len(usage_types))
   #a list of our usage_points, in the list individually round them off to the 2nd decimal  
   usage_points = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)] 
   plt.bar(y_pos, usage_points, align='center', alpha=0.5)
   plt.xticks(y_pos, usage_types)
   #this title appears on the left hand side of our graph, showing exactly what we are trying to graph
   plt.ylabel('Usage Amount')
   #the title of our graph
   plt.title(f"Storage Overview for {user_acc} {get_daydate}")
   #this will allow us to interact with our graph, if you hover over a bar in the graph - it will show a value
   mplcursors.cursor()
  
   
#generate our piechart 
def gen_piGraph():
    usage_labels = 'Storage Capacity', 'Used Space', 'Remaining Space'
    usage_sizes = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)]
    #we will need this to show our plot - also give window title for pie chart
    fig1, ax1 = plt.subplots(num="Storage Pie Chart")
    plt.title(f"Storage Overview for {user_acc} {get_daydate}")
    #Explode Remaining Space section of Pie Graph
    #explode = (0,0,0.2) - removed explode=explode from ax1.pie()
    ax1.pie(usage_sizes, labels=usage_labels, autopct='%1.1f%%',shadow=True, startangle=90)
    #ensure that our graph is drawn as circle
    ax1.axis('equal')  
    mplcursors.cursor()
   

def get_args(chart_choice):
    parser = argparse.ArgumentParser()
    parser.add_argument("--barchart", help="Usage: --barchart barchart, --piechart piechart, --chstorage chstorage")
    parser.add_argument("--piechart")
    parser.add_argument("--chstorage") #check if remaining storage is at a safe level, if not, show notification. --chstorage is short for checkstorage
    args = parser.parse_args()
    if args.barchart:
        print(f'Launching {args.barchart}..')
        plt.show(graph_space())
    elif args.piechart:
        print(f'Launching {args.piechart}..')
        plt.show(gen_piGraph()) 
    elif args.chstorage:
        #[Complete] I need to figure out how we can check if the amount of remaining storage is LESS than or equal to 10GB.
        #[Complete] I need to get minspace_amount to readable value, so we can compare our two values, remainingspace_amount & minspace_amount.
        #[Objective] I need to implement notification to warn user if remainingspace_amount is less than the min_gb_value.
        if remainingspace_amount > min_gb_value:
            print(f"You have {round(remainingspace_amount,2)} GB which is greater than the minimum amount needed of {round(min_gb_value,2)} GB")    
            notification = Notify()
            notification.title = "Storage level Safe"
            notification.message = "You have a safe level of remaining storage"
            notification.send()    
        elif remainingspace_amount < min_gb_value:
            print(f"You have {round(remainingspace_amount,2)} GB which is less than the minimum amount needed of {round(min_gb_value,2)} GB")
            notification_notsafe = Notify()
            notification_notsafe.title = "Storage level Warning"
            notification_notsafe.message = f"Warning: Remaining Storage levels are low, you have: {round(remainingspace_amount,2)} GB left."
            notification_notsafe.send()


get_account()  
get_platform()
usageper_core()
get_capacity(my_path)
get_usedSpace(my_path)
get_TotalSpace(my_path)
get_args(chart_choice)
graph_space()
gen_piGraph()

