# Py Storage Tracker
Py Storage Tracker is a cross-platform command line tool written in Python 3 to help track storage of your device! This is a project being actively developed by Milos Vuksanovic, over time I will continue to add more features and functionality. Feel free to play around with this project, test it etc :-).

I'll add outputs from two machines, my personal PC Windows 10 & also my Macbook Pro.
#The output of Python Storage Tracker:
#[Windows 10]
On Windows cmd when python s_tracker.py is first run:
![first_screen](https://user-images.githubusercontent.com/18017763/110236803-f9057c00-7f8b-11eb-8610-1934ba2db3bb.PNG)

python s_tracker.py --help shows all  commands currently available:
![new_help](https://user-images.githubusercontent.com/18017763/110237641-1ee14f80-7f91-11eb-84bf-0b846ba5256e.PNG)

python s_tracker.py -b b (b is short for barchart) | python s_tracker.py --barchart barchart is also acceptable:
![b_chart](https://user-images.githubusercontent.com/18017763/110237016-a0cf7980-7f8d-11eb-9864-caa65cd13f9e.PNG)

python s_tracker.py -p p (p is short for piechart) | python s_tracker.py --piechart piechart is also acceptable:
![p_chart](https://user-images.githubusercontent.com/18017763/110237035-c2c8fc00-7f8d-11eb-8dcd-a0ebb096ea31.PNG)

python s_tracker.py -cs cs (cs is short for check storage) | python s_tracker.py --chstorage chstorage is also acceptable:
This command also can send through a notification, it checks to see if your remaining storage is less than 10GB, if it is it will send through a notification.
![check_storage](https://user-images.githubusercontent.com/18017763/110237105-0d4a7880-7f8e-11eb-8a8d-5dc3bda932e2.PNG)

python s_tracker.py -ac ac (ac is short for all charts) | python s_tracker.py --all_charts all_charts is also acceptable:
this command opens both charts, however once one is closed - the other will appear.

python s_tracker.py -od od (od is short for other drives) python s_tracker.py --other_drives other_drives is also acceptable:
shows all drives, in this case I will show two examples. 

#first: 2GB USB inserted
![other_drives](https://user-images.githubusercontent.com/18017763/110237300-6f57ad80-7f8f-11eb-840f-3fc990382888.PNG)

#Second: no usb 
![no_usb_od](https://user-images.githubusercontent.com/18017763/110237331-9ada9800-7f8f-11eb-9dab-a3b6edbba5aa.PNG)

python s_tracker.py -dc dc (dc is short for drive count) | python s_tracker.py --drive_count drive_count is also acceptable:
The purpose of this command is to return the amount of drives & return file systems -

I'll demonstrate with and without 2GB USB inserted:
![dc_noUSB](https://user-images.githubusercontent.com/18017763/110237498-8b0f8380-7f90-11eb-9a23-d5d247fe28c9.PNG)

With inserted 2gb USB:
![dc_usb_inserted](https://user-images.githubusercontent.com/18017763/110237500-8c40b080-7f90-11eb-9980-c3516d30ebbb.PNG)









