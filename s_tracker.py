import os 
import sys 
import datetime 
import shutil 
import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
import mplcursors 
from os import path
import platform 
import psutil
import argparse
from notifypy import Notify
from pathlib import Path
import warnings
import pickle 
from datetime import date
import logging
import calendar as c
from time import gmtime, strftime
import time

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

#note min_gb_value = 10gb
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

#ignore warnings - This should fix the MatplotlibDeprecationWarning
warnings.filterwarnings("ignore", category=UserWarning)

def get_account():   
    #time_acc = datetime.datetime.now()
    t = date.today()
    m_d = date.today()
    day = c.day_name[m_d.weekday()] #return the day of week
    t_n = strftime("%H:%M:%S",gmtime())
    time_now = t.strftime(f"{day} %B %d")
    print(f"User: {user_acc}")
    print(f"Last login: ", time_now, t_n)      
    

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
    #we should look at adding the larger format very similar to the windows format of space.
    #print(f'Capacity: {:6.2f} GB \n'.format(free_b/gb))
    print('Capacity: {:6.2f} GB'.format(free_b/gb), "| {:,} bytes".format(free_b))
    

#print used space in Bytes    
def get_usedSpace(my_path):
      #we should look at adding the larger format very similar to the windows format of space.
      #print(f"Used Space: {used_b} \n")
      print('Used space: {:6.2f} GB'.format(used_b/gb), "| {:,} bytes".format(used_b) )


#print remaining in Bytes
def get_TotalSpace(my_path):
    #print(f"Total Space: {total_b} \n")
    #we should look at adding the larger format very similar to the windows format of space.
   # print('Remaining: {:6.2f} GB'.format(total_b/gb))
    if total_b/gb < min_gb_value: #if less than min_gb_value or 10GB, print with Warning message beside Remaining amount & indicator '*'////// ->  f"| {total_b} bytes. HERE
        print('*Free space: {:6.2f} GB'.format(total_b/gb), '\n' ,f'\n[Warning] {user_acc}, you are running low on Free storage.', "| {:,} bytes".format(total_b) ,'\n')
    elif total_b/gb > min_gb_value: #if greater than min_gb_value or 10GB, print it normally without warning message.
        print('Free space: {:6.2f} GB'.format(total_b/gb), "| {:,} bytes".format(total_b))    


def graph_space():
   bargraphwin_title = plt.figure(f"Storage Bar Chart {user_acc}")  
   #here i have given what needs to be put in the graph, what we are graphing
   usage_types = (f'Capacity \n {round(storage_capacity_amount,2)} GB', f'Used Space \n {round(usedspace_amount,2)} GB', f'Free Space \n {round(remainingspace_amount,2)} GB')
   #arange our space types 
   y_pos = np.arange(len(usage_types))
   #a list of our usage_points, in the list individually round them off to the 2nd decimal  
   usage_points = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)] 
   plt.bar(y_pos, usage_points, align='center', alpha=0.5)
   plt.xticks(y_pos, usage_types)
   #this title appears on the left hand side of our graph, showing exactly what we are trying to graph
   plt.ylabel('Usage Amount (GB)')
   #the title of our graph
   plt.title(f"Storage Overview for {user_acc}")
   #this will allow us to interact with our graph, if you hover over a bar in the graph - it will show a value
   mplcursors.cursor()
   
   
def gen_piGraph():
    usage_labels = f'Capacity {round(storage_capacity_amount,2)} GB', f'Used Space {round(usedspace_amount,2)} GB', f'Free Space {round(remainingspace_amount,2)} GB'
    usage_sizes = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)]
    #we will need this to show our plot - also give window title for pie chart
    fig1, ax1 = plt.subplots(num=f"Storage Pie Chart {user_acc}")
    plt.title(f"Storage Overview for {user_acc}" , loc="left")
    #Explode Remaining Space section of Pie Graph
    #explode = (0,0,0.2) - removed explode=explode from ax1.pie()
    ax1.pie(usage_sizes, labels=usage_labels, autopct='%1.1f%%',shadow=False, startangle=90)
    #ensure that our graph is drawn as circle
    ax1.axis('equal')  
    mplcursors.cursor()
   

def get_args(): #chart_choice - this was a param at one point, but removed since not needed.
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--barchart")
    parser.add_argument("-p","--piechart")
    parser.add_argument("-cs","--chstorage")  #cs = check storage with notification.
    parser.add_argument("-ac","--all_charts")
    args = parser.parse_args()
    if args.barchart:
        print(" ")
        print(f'Launching --{args.barchart}')
        plt.show(graph_space())
    elif args.piechart:
        print(" ")
        print(f'Launching --{args.piechart}')
        plt.show(gen_piGraph()) 
    elif args.chstorage:
        print(" ")
        if remainingspace_amount > min_gb_value:
            print(f"You have {round(remainingspace_amount,2)} GB remaining which is greater than the minimum amount needed of {round(min_gb_value,2)} GB")    
            notification = Notify()
            notification.title = "Free Storage levels Safe"
            notification.message = f"You have {round(remainingspace_amount,2)} GB of Free storage available"
            notification.send()    
        elif remainingspace_amount < min_gb_value:
            print(f"You have {round(remainingspace_amount,2)} GB which is less than the minimum amount needed of {round(min_gb_value,2)} GB")
            notification_notsafe = Notify()
            notification_notsafe.title = "Free Storage levels Low"
            notification_notsafe.message = f"Warning: Free Storage levels are low, You have {round(remainingspace_amount,2)} GB remaining."
            notification_notsafe.send()
    elif args.all_charts:
        print(" ")
        print(f"Launching --{args.all_charts}") 
        plt.show(graph_space())
        plt.show(gen_piGraph())
        
   

print(" ")
get_account()  
get_platform()
usageper_core()
get_capacity(my_path)
get_usedSpace(my_path)
get_TotalSpace(my_path)
get_args()
graph_space()
gen_piGraph()
print(" ")


     


