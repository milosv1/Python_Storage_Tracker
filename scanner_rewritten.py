#first imported items
import os
import sys
import datetime
import shutil

#function to get user account & time accessed
def get_account():
    #get users account username
    user_acc = os.getlogin()
    #get time accessed
    time_acc = datetime.datetime.now()
    #print username logged in
    print(f"User: {user_acc}")
    #print time accessed - now
    print(f"Last accessed:{time_acc}")


#call get_account function
get_account()    