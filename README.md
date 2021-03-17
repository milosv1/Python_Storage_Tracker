# Py Storage Tracker
Py Storage Tracker is a cross-platform command line tool written in Python 3 to help track storage of your device! This is a project being actively developed by Milos Vuksanovic, over time I will continue to add more features and functionality. Feel free to play around with this project, test it etc :-).

This program runs on both of my machines, my personal computer which is running on Windows 10 & also my Macbook Pro.

[Updated on 17/03/2021] On Windows cmd when python s_tracker.py is first run:
![startup_screen](https://user-images.githubusercontent.com/18017763/111435375-d37b2e00-8754-11eb-97f0-df536c015c34.png)


python s_tracker.py --help shows all  commands currently available:
![new_help](https://user-images.githubusercontent.com/18017763/110237641-1ee14f80-7f91-11eb-84bf-0b846ba5256e.PNG)


[Updated on 17/03/2021] python s_tracker.py -b b (b is short for barchart) | python s_tracker.py --barchart barchart is also acceptable:
![new barchart](https://user-images.githubusercontent.com/18017763/111435667-2b199980-8755-11eb-9afb-289f269cca0d.png)


[Updated on 17/03/2021] python s_tracker.py -p p (p is short for piechart) | python s_tracker.py --piechart piechart is also acceptable:
![new piechart](https://user-images.githubusercontent.com/18017763/111435775-4f757600-8755-11eb-8c20-641ff9cfbadf.png)


python s_tracker.py -cs cs (cs is short for check storage) | python s_tracker.py --chstorage chstorage is also acceptable:
This command also can send through a notification, it checks to see if your remaining storage is less than 10GB, if it is it will send through a notification.
![check_storage](https://user-images.githubusercontent.com/18017763/110237105-0d4a7880-7f8e-11eb-8a8d-5dc3bda932e2.PNG)


python s_tracker.py -ac ac (ac is short for all charts) | python s_tracker.py --all_charts all_charts is also acceptable:
this command opens both charts, however once one is closed - the other will appear.


python s_tracker.py -od od (od is short for other drives) python s_tracker.py --other_drives other_drives is also acceptable:
shows all drives, in this case I will show two examples. 
[Quick note] - I have made some small changes to how output shows (for python s_tracker.py -od od OR python s_tracker.py --other_drives other_drives). I have also added output for the File System & Description of each Drive listed.

[Updated on 14/03/2021] 2GB USB inserted:
![updated OD with USB2 2](https://user-images.githubusercontent.com/18017763/111057414-7aed2c00-84db-11eb-9902-185aed56a2e1.png)


[Updated on 14/03/2021] No USB inserted: 
![UPDATED no USB OD](https://user-images.githubusercontent.com/18017763/111057300-7116f900-84da-11eb-9c60-4f13757e6d8a.png)


python s_tracker.py -dc dc (dc is short for drive count) | python s_tracker.py --drive_count drive_count is also acceptable:
The purpose of this command is to return the amount of drives & return file systems.


Without 2GB USB inserted:
![dc_noUSB](https://user-images.githubusercontent.com/18017763/110237498-8b0f8380-7f90-11eb-9a23-d5d247fe28c9.PNG)


With inserted 2GB USB:
![dc_usb_inserted](https://user-images.githubusercontent.com/18017763/110237500-8c40b080-7f90-11eb-9980-c3516d30ebbb.PNG)









