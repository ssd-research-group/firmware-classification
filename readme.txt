Welcome to ssd_tst! 

For any issues not addressed below or specific problems with the code please email varon.alext@gmail.com and your problem will be addressed as quickly as possible.

How do I use ssd_tst?

	>> python ssd_tst.py [-rwzlLsSRch] 
	
	-h : help.	Will list out the options for usage
	
	-r : readFile.	Tell the program how many read trials you would like to perform 
			Default = 0
					
	-w : writeFile.	Tell the program how many write trials you would like to perdom
			Default = 0
					
	-z : size.	Tell the program what size files you want to test (in MB).
			The expected format is size1,size2,size3
			If the file does not currently exist then the program will create it.
			Default = 4 (MB)

	-l : location.	Tell the program where the original files are stored (this should be on the D: drive)
			Default = current working directory (so run it from the D: drive!)
					
	-L : remote_location. 	Tell the program where you want to read and write files from/to.
				Default = C:\\Users\sansungssd\Desktop\
	
	-p : start_serial_port.	Tell the program what serial num/port you are using to communicate with.
				A message will be sent on this channel to start running the data collection.
				Syntax is serial_num,port
				Default = COM13,9600

	-P : stop_serial_port.	Tell the program what serial num/port you are using to communicate with.
				A message will be sent on this channel to stop running the data collection.
				Syntax is serial_num,port
				Default = COM12,9600

	-R : record_time.	Tell the program how long you want to record data.
				*Note, this is how much time before and after data collection!
				default = 200 (measured in seconds)

	-c : create_file. 	Tell the program a file size (in MB) and it will create it.
				Example: 5 (this would export a file called 5MB)

	-s : seed.	Tell the program the name of the file containing the seed that you are using to create random files

	-S : create_seed.	Tell the program to create a seed file.

Common usage

	>> python ssd_tst.py -r 10 -w 8 -z 6,24,64,256 -L C:\\Users\diff_user\Desktop\

	This will run the program for 10 read trials/ 8 write trials on each of the four listed file sizes reading and writing to a new remote location.

	>> python ssd_tst.py -c 20
	
	This will create a new file, 20 MB large, called 20MB.txt

	>> python ssd_tst.py -S

	THis will create a new seed file called seed.txt

