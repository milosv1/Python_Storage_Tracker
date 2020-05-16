#first imported items
import os
import sys
import datetime
import shutil

#calc
#gb = 10 ** 9 - global

#get users account username - global
user_acc = os.getlogin()

#path needed - global - '/' root directory
my_path = '/'

#function to get user account & time accessed
def get_account():
    #get time accessed
    time_acc = datetime.datetime.now()
    #print username logged in
    print(f"User: {user_acc}")
    #print time accessed - now
    print(f"Last accessed: {time_acc}")

#get capacity - in Bytes
def get_capacity(my_path):
    free_b,used_b,total_b = shutil.disk_usage(my_path)
    print(f"Capacity: {free_b} \n")
    #print('{:6.2f} GB'.format(TOTAL_AMOUNT))
    
    
  


#call get_account function
get_account()   
#get capacity 
get_capacity(my_path)