import os
import sys 
import datetime
from datetime import date
import shutil 
import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
import mplcursors 
import platform 
import psutil
import argparse
from notifypy import *
#from notifypy import Notify
from pathlib import *
import warnings 
import calendar as c
from time import *
import cpuinfo
import locale
import urllib.request


gb = 10 ** 9
#print("GB VALUE:",gb) 

user_acc = os.getlogin()

get_daydate = datetime.datetime.now()

system_name = platform.node()

#root directory for C:
my_path = '/'

free_b,used_b,total_b = shutil.disk_usage(my_path)

#Outputs for C:
storage_capacity_amount = free_b/gb
usedspace_amount = used_b/gb
remainingspace_amount = total_b/gb

#10gb = 10,737,418,240 bytes
minspace_amount = 1024**3*10  

#note min_gb_value = 10gb
min_gb_value = minspace_amount/gb

user_platform = sys.platform

user_platform_rel = platform.release()

physicalcore_count = psutil.cpu_count(logical=False)
totalcore_count = psutil.cpu_count(logical=True)

bytes_sent = psutil.net_io_counters().bytes_sent
bytes_recv = psutil.net_io_counters().bytes_recv

per_cpu = psutil.cpu_percent(percpu=True, interval=1)

platform_pro = cpuinfo.get_cpu_info()['brand_raw']

chart_choice = ''

warnings.filterwarnings("ignore", category=UserWarning)

loc = locale.getlocale()

get_sys_lang = locale.getdefaultlocale()[0]

last_reboot = psutil.boot_time()

#-------------------------------------------------

def greeting():
    greetings = """
Welcome to the Python Storage Tracker ~
A side project being actively developed by Milos Vuksanovic.

* To start: In your windows 10 command line type: python s_tracker.py --help
* To start on macOS: In your Mac Terminal type: python3 s_tracker.py --help
- to view a list of commands available.
    """
    return greetings

#-------------------------------------------------

def get_account():   
    t = date.today()
    m_d = date.today()
    day = c.day_name[m_d.weekday()] #return the day of week
    t_n = strftime("%H:%M:%S",gmtime())
    time_now = t.strftime(f"{day} %B %d")
    print(f"User: {user_acc}")
    print(f"Last login: ", time_now, t_n) 
    print(f"Last reboot: {datetime.datetime.fromtimestamp(last_reboot)}")     


#-------------------------------------------------

def get_platform(): 
    print(f"Computer Name: {system_name}")
    print(f"Platform: {user_platform}")
    print(f"Platform Release: {user_platform_rel}")
    print(f"Language: {get_sys_lang}")
    if os.name == "nt":
        #this code is nt/Windows specific
        import wmi
        c_m = wmi.WMI()
        systeminfo = c_m.Win32_ComputerSystem()[0]
        Manufacturer = systeminfo.Manufacturer
        graphics_card = c_m.Win32_VideoController()[0]
        g_r = psutil.virtual_memory()[0]
        print("Total RAM: {:,} bytes".format(g_r)) 
        print(f"System Manufacturer: {Manufacturer}")
        print('Graphics Card: {0}'.format(graphics_card.Name))
    elif os.name == "posix":
        #this code is POSIX specific - When you run on Mac, You'll get the following output
        g_m = psutil.virtual_memory()[0]
        print("Total Memory: {:,} bytes".format(g_m)) 
    print(f"Processor: {platform_pro} \n")
    print(f"Active Internet Connection: {test_internet_connection()}")
    print(f'Total Bytes Sent: {get_size(bytes_sent)}')
    print(f'Total Bytes Recieved: {get_size(bytes_recv)} \n')
    print(f'Physical Core Count: {physicalcore_count}')
    print(f'Total Core Count: {totalcore_count}')
    

#-------------------------------------------------

#this function  converts larger numbers into - Kilobytes - MegaBytes - Gigabytes - TeraBytes - PetaBytes
def get_size(bytes, suffix="B"):
    fact = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < fact:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= fact


#-------------------------------------------------

#Get % of usage per core & total CPU usage %
def usageper_core():
    for i, percentage in enumerate(per_cpu):
      print(f'Core {i}: {percentage}%')
    print(f'Total CPU Usage: {psutil.cpu_percent()}% \n')   


#-------------------------------------------------

def get_capacity(my_path):    
    print('Capacity: {:6.2f} GB'.format(free_b/gb), "| {:,} bytes".format(free_b)) 
    

#-------------------------------------------------

def get_usedSpace(my_path):
      print('Used space: {:6.2f} GB'.format(used_b/gb), "| {:,} bytes".format(used_b))


#-------------------------------------------------

def get_TotalSpace(my_path):
    if total_b/gb < min_gb_value: #if less than min_gb_value or 10GB, print with Warning message beside Remaining amount & indicator '*'
        print('[Warning!]Free space: {:6.2f} GB'.format(total_b/gb), "| {:,} bytes".format(total_b), '\n' ,f'\n[Warning] {user_acc}, Your storage is almost full.','\n')
    elif total_b/gb > min_gb_value: #if greater than min_gb_value or 10GB, print it normally without warning message.
        print('Free space: {:6.2f} GB'.format(total_b/gb), "| {:,} bytes".format(total_b))    


#-------------------------------------------------

def graph_space():
   #Create a barchart to visualise storage
   t = date.today()
   m_d = date.today()
   day = c.day_name[m_d.weekday()] 
   t_n = strftime("%H:%M:%S",gmtime())
   time_now = t.strftime(f"{day} %B %d") 
   bargraphwin_title = plt.figure(f"Storage Bar Chart")  
   usage_types = (f'Capacity \n {round(storage_capacity_amount,2)} GB', f'Used Space \n {round(usedspace_amount,2)} GB', f'Free Space \n {round(remainingspace_amount,2)} GB') 
   y_pos = np.arange(len(usage_types)) 
   usage_points = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)] 
   plt.bar(y_pos, usage_points, align='center', alpha=0.5)
   plt.xticks(y_pos, usage_types)
   plt.ylabel('Usage Amount (GB)')
   plt.title(f"Storage Overview for {user_acc} on {time_now} at {t_n}")
   mplcursors.cursor()
   
#-------------------------------------------------
   
def gen_piGraph():
    #Create a pie chart to visualise storage
    t = date.today()
    m_d = date.today()
    day = c.day_name[m_d.weekday()] 
    t_n = strftime("%H:%M:%S",gmtime())
    time_now = t.strftime(f"{day} %B %d") 
    usage_labels = f'Capacity {round(storage_capacity_amount,2)} GB', f'Used Space {round(usedspace_amount,2)} GB', f'Free Space {round(remainingspace_amount,2)} GB'
    usage_sizes = [round(storage_capacity_amount,2), round(usedspace_amount,2), round(remainingspace_amount,2)]
    fig1, ax1 = plt.subplots(num=f"Storage Pie Chart")
    plt.title(f"Storage Overview for {user_acc} on {time_now} at {t_n}" , loc="left")
    #explode = (0,0,0.2) - removed explode=explode from ax1.pie()
    ax1.pie(usage_sizes, labels=usage_labels, autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')  
    mplcursors.cursor()

#-------------------------------------------------

def mem_Chart():
    #Creates a piechart that visualises used memory & remaining memory
    t = date.today()
    d_t = date.today()
    day = c.day_name[d_t.weekday()]
    t_n = strftime("%H:%M:%S",gmtime())
    time_now = t.strftime(f"{day} %B %d")
    u_m = psutil.virtual_memory().percent #used memory
    t_m = psutil.virtual_memory().total #total memory
    a_m = psutil.virtual_memory().available * 100 / t_m
    labels = f'Used memory {round(u_m,2)}%', f'Available memory {round(a_m,2)}%' 
    mem_sizes = [round(u_m,2), round(a_m,2)]
    fig1, ax1 = plt.subplots(num=f"Memory Used/Available")
    plt.title(f"Memory Used/Available for {user_acc} on {time_now} at {t_n}", loc="left")
    ax1.pie(mem_sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    mplcursors.cursor()
    
#-------------------------------------------------

def clear():
 if os.name == "nt":
    os.system("cls")
 else:
     os.system("clear")   

#-------------------------------------------------

def test_internet_connection():
    try:
        urllib.request.urlopen('https://www.google.com', timeout=5)
        return True
    except:
        return False
 
#-------------------------------------------------

def get_args(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--barchart")
    parser.add_argument("-p","--piechart")
    parser.add_argument("-m","--memchart")
    parser.add_argument("-cs","--chstorage")  
    parser.add_argument("-od","--other_drives") 
    parser.add_argument("-dc","--drive_count") 
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
            print(f"You have {round(remainingspace_amount,2)} GB of Free space remaining.")    
            notification = Notify()
            notification.title = "Safe storage levels"
            notification.message = f"You have {round(remainingspace_amount,2)} GB of Free space available."
            notification.send()    
        elif remainingspace_amount < min_gb_value:
            print(f"You have {round(remainingspace_amount,2)} GB of Free space remaining.")
            notification_notsafe = Notify()
            notification_notsafe.title = "Low storage"
            notification_notsafe.message = f"[Warning] - Your storage is almost full."
            notification_notsafe.send()
    elif args.other_drives:
        clear()
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"Drive {partition.device}")
            print('--------------------------------------')
            free_b_a,used_b_a,total_b_a = shutil.disk_usage(partition.device)
            print('Capacity: {:6.2f} GB'.format(free_b_a/gb),'| {:,} bytes'.format(free_b_a))
            print('Used space: {:6.2f} GB'.format(used_b_a/gb),'| {:,} bytes'.format(used_b_a))
            print('Free space: {:6.2f} GB'.format(total_b_a/gb),'| {:,} bytes'.format(total_b_a))
            print(f'File System  {partition.fstype}')
            print(f'Description  {partition.opts}')
            print('--------------------------------------','\n')  
    elif args.drive_count:
        clear()
        found_partition = 0
        found_fstypes = 0
        partition_list = []
        fstype_list = []
        partitions = psutil.disk_partitions()
        for partition in partitions:
            found_partition+=1
            found_fstypes+=1
            partition_list.append(partition.device)
            fstype_list.append(partition.fstype)
        if len(partition_list) > 1:
            print("More than one drive?: ", True)
            print("Drives in List: ", len(partition_list))
            print(f"Drives Found: {partition_list} \n")
            print(f"File systems in List:", len(fstype_list))
            print(f"File systems Found: {fstype_list}")
        elif len(partition_list) < 2:
            print("There is only one drive.")  
    elif args.memchart:
        print(f"Launching --{args.memchart}")
        plt.show(mem_Chart())       

 #-------------------------------------------------
     
def main():
    clear()
    greeting()
    get_account() 
    get_platform()
    usageper_core()
    get_capacity(my_path)
    get_usedSpace(my_path)
    get_TotalSpace(my_path)
    get_args()
    graph_space()
    gen_piGraph()
    mem_Chart()
    print("")

 #-------------------------------------------------

if __name__ == "__main__":                    
   main()
