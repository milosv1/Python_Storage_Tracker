# Python Storage Tracker
As of 10/06/2020 my command line tool allows for command line arguments, for example when you direct yourself to the repository containing the file, simply run the following python s_tracker.py this will allow you to view information such as host name, network info bytes sent/bytes recieved - information on cores, storage info. running the following command python s_tracker.py -h shows what other arguments are available to run, this is essentially the help command. The other arguments available are python s_tracker.py --piechart piechart & python s_tracker.py --barchart barchart both show the data visually.

As of 20/07/2020, we currently have significant progress, right now the main objective is to compare IF remainingspace_amount is lessthan or equal to minspace_amount, minspace_amount will have the value of 10gb, which is 10gb = 10,737,418,240. We need to shorten this bigger value, then compare the pair.

Implemented comparison of remainingspace_amount and minspace_amount, when the --chstorage chstorage is input into the command line, it will check if your remaining amount of space is less than 10GB, or if your remainingspace_amount is greater than 10GB. Next we need to implement notification for less than statement to warn user. Notifications have been implemented, when the --chstorage chstorage OR -cs cs are entered a notification will be shown displaying how much remaining storage the user has compared to the 10GB threshold amount.

14/09/2020 - Recently i've made changes to the look of the terminal look, especially the 'last login: ... ' section, this was inspired by the Terminal of the Mac OS.

