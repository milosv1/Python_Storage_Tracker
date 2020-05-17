#first imported items
import os
import sys
import datetime
import shutil
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import mplcursors
#calc
gb = 10 ** 9 #- global

#get users account username - global
user_acc = os.getlogin()

#get time & date
get_daydate = datetime.datetime.now()

#path needed - global - '/' root directory
my_path = '/'

#new Global
free_b,used_b,total_b = shutil.disk_usage(my_path)

#calculations total = total_b/gb
#Used = used_b / gb
#free = free_b / gb
#global calcs
free_amount = free_b/gb
used_amount = used_b/gb
total_amount = total_b/gb

#test! it works! - rounds to 2 decimal places
#print(f"{round(free_amount,2)}")


#function to get user account & time accessed
def get_account():
    #get time accessed
    time_acc = datetime.datetime.now()
    #print username logged in
    print(f"User: {user_acc}")
    #print time accessed - now
    print(f"Last accessed: {time_acc} \n")

#print capacity - in Bytes
def get_capacity(my_path):    
    #print(f'Capacity: {:6.2f} GB \n'.format(free_b/gb))
    print('{:6.2f} GB'.format(free_b/gb))
    
#print used space in Bytes    
def get_usedSpace(my_path):
      #print(f"Used Space: {used_b} \n")
      print('{:6.2f} GB'.format(used_b/gb) )

#print total in Bytes
def get_TotalSpace(my_path):
    #print(f"Total Space: {total_b} \n")
    print('{:6.2f} GB'.format(total_b/gb))

#show space in bar chart - also interactive
def graph_space():
   usage_types = ('Free Space', 'Used Space', 'Total Space')
   y_pos = np.arange(len(usage_types))  
   usage_points = [round(free_amount,3),round(used_amount,3),round(total_amount,3)] 

   plt.bar(y_pos, usage_points,align='center', alpha=0.5)
   plt.xticks(y_pos, usage_types)
   plt.ylabel('Usage Amount')
   plt.title(f"Space Overview for {user_acc} {get_daydate}")
   mplcursors.cursor()
   plt.show()

#call get_account function
get_account()   
#get capacity 
get_capacity(my_path)
#get_usedSpace
get_usedSpace(my_path)
#get total space in byes
get_TotalSpace(my_path)
#show graph
graph_space()