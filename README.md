# Py Storage Tracker
Py Storage Tracker is a cross-platform command line tool using Python to track storage and other system related information. The command line 
tool also features the ability to be able to display storage data visually through either a Bar Chart or Pie Chart.

[Updated on 18/03/2021] On Windows cmd when python s_tracker.py is first run:
To output RAM/Memory, it checks to see if you're on Windows or MacOS, If you are on Windows it will output Total RAM, However if you are on MacOS it will output Total Memory.

Recently added output for graphics card, however this will only appear if ran on a Windows machine.

![Added graphics card output ](https://user-images.githubusercontent.com/18017763/116358725-4cd06b00-a841-11eb-9269-0e1edd30472a.png)

Example output output of what is shown in the instance you have less than 10GB available.

<img width="810" alt="Mac outputs" src="https://user-images.githubusercontent.com/18017763/111594295-feca4f80-881e-11eb-9955-360695c885de.png">

python s_tracker.py --help displays all commands currently available:

![new_help](https://user-images.githubusercontent.com/18017763/110237641-1ee14f80-7f91-11eb-84bf-0b846ba5256e.PNG)

[Updated on 17/03/2021] python s_tracker.py -b b (b is short for barchart) | python s_tracker.py --barchart barchart is also acceptable:

![new barchart](https://user-images.githubusercontent.com/18017763/111435667-2b199980-8755-11eb-9afb-289f269cca0d.png)

[Updated on 17/03/2021] python s_tracker.py -p p (p is short for piechart) | python s_tracker.py --piechart piechart is also acceptable:

![new piechart](https://user-images.githubusercontent.com/18017763/111435775-4f757600-8755-11eb-8c20-641ff9cfbadf.png)

[Updated on 17/04/2021] python s_tracker.py -m m (m is short for memchart) | python s_tracker.py --memchart memchart is also acceptable:

![mem used and available](https://user-images.githubusercontent.com/18017763/115108496-27776d80-9fb4-11eb-8fd1-b6cf7b98fe00.png)

python s_tracker.py -cs cs (cs is short for check storage) | python s_tracker.py --chstorage chstorage is also acceptable:
In the scenario that you have less than 10GB available in your machine, a notification will be shown.

![check_storage](https://user-images.githubusercontent.com/18017763/110237105-0d4a7880-7f8e-11eb-8a8d-5dc3bda932e2.PNG)



python s_tracker.py -od od (od is short for other drives) python s_tracker.py --other_drives other_drives is also acceptable:
shows all drives, in this case I will show two examples. 
[Note] - I have made some small changes to how output shows (for python s_tracker.py -od od || python s_tracker.py --other_drives other_drives). I have also added output for the File System & Description of each Drive listed.


[Updated on 03/04/2021] 2GB USB inserted example:

![o_d with usb NEW 2](https://user-images.githubusercontent.com/18017763/113476911-321d0780-94ca-11eb-8fef-711ae8c54009.jpg)


[Updated on 03/04/2021] No USB inserted example: 

![o_d no usb NEW](https://user-images.githubusercontent.com/18017763/113476945-67c1f080-94ca-11eb-850f-3a1c21d582e6.png)


[Updated on 16/04/2021] Inserted 1tb seagate hard drive example:

![new -od command](https://user-images.githubusercontent.com/18017763/114962765-abdfc880-9eae-11eb-8e3b-bf5799aa134b.png)


python s_tracker.py -dc dc (dc is short for drive count) | python s_tracker.py --drive_count drive_count is also acceptable:
The purpose of this command is to return the amount of drives & return file systems.


Without 2GB USB inserted example:

![dc_noUSB](https://user-images.githubusercontent.com/18017763/110237498-8b0f8380-7f90-11eb-9a23-d5d247fe28c9.PNG)


With inserted 2GB USB example:

![dc_usb_inserted](https://user-images.githubusercontent.com/18017763/110237500-8c40b080-7f90-11eb-9980-c3516d30ebbb.PNG)


[Updated on 16/04/2021] With inserted 1TB Seagate hard drive example:

![dc command ](https://user-images.githubusercontent.com/18017763/114962616-5b686b00-9eae-11eb-837d-87263ef7b11e.png)










