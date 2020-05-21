#first imported items
import os #operating system
import sys #system
import datetime #get date and time
import shutil #allows us to work with files 
import matplotlib.pyplot as plt; plt.rcdefaults() #allows us to implement graphs and charts
import numpy as np #numpy- allows us to work with maths
import mplcursors # this is a new import allows us to interact with bar chart 

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
#global calcs - here we get the free amount, used amount and also the remaining
free_amount = free_b/gb
used_amount = used_b/gb
remaining_amount = total_b/gb

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
    #here i have given what needs to be put in the graph, what we are graphing
   usage_types = ('Storage Capacity', 'Used Space', 'Remaining Space')
   #arange our space types 'in order'?
   y_pos = np.arange(len(usage_types))
   #a list of our usage_points, in the list individually round them off to the 3rd decimal  
   usage_points = [round(free_amount,3),round(used_amount,3),round(remaining_amount,3)] 

   #How we want our bar chart to look
   plt.bar(y_pos, usage_points,align='center', alpha=0.5)
   plt.xticks(y_pos, usage_types)
   #this title appears on the left hand side of our graph, showing exactly what we are trying to graph
   plt.ylabel('Usage Amount')
   #the title of our graph
   plt.title(f"Space Overview for {user_acc} {get_daydate}")
   #this will allow us to interact with our graph, if you hover over a bar in the graph - it will show a value
   mplcursors.cursor()
   #finally show our graph
   plt.show()

#generate our piechart - the pie chart is generated once the bar graph is closed
def gen_piGraph():
    # usage_labels is what parts of the pie chart will be called
    usage_labels = 'Storage Capacity', 'Used Space', 'Remaining Space'
    #the usage sizes should be rounded to 3 decimal points - this does not work %100 right now
    usage_sizes = [round(free_amount,3),round(used_amount,3),round(remaining_amount,3)]
    #we will need this to show our plot
    fig1, ax1 = plt.subplots()
    #what piechart will feature
    ax1.pie(usage_sizes,labels=usage_labels, autopct='%1.1f%%',shadow=True, startangle=90)
    #ensure that our graph is drawn as circle
    ax1.axis('equal')  
    #generate the pie chart
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
#generate pie graph - this is displayed once the bar graph is closed!
gen_piGraph()