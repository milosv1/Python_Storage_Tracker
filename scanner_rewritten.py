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

#new Global
free_b,used_b,total_b = shutil.disk_usage(my_path)

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
    print(f"Capacity: {free_b} \n")
    #print('{:6.2f} GB'.format(TOTAL_AMOUNT))
    
#print used space in Bytes    
def get_usedSpace(my_path):
      print(f"Used Space: {used_b} \n")

#print total in Bytes
def get_TotalSpace(my_path):
    print(f"Total Space: {total_b} \n")

#call get_account function
get_account()   
#get capacity 
get_capacity(my_path)
#get_usedSpace
get_usedSpace(my_path)
#get total space in byes
get_TotalSpace(my_path)