#!/usr/bin/env python
import time, os, argparse, ctypes, sys, random, platform, subprocess, shutil, getopt
from sys import platform as _platform

err_file = open("error_file_"+'_'.join([str(time.localtime()[j]) for j in range(5)])+'.txt','w')
ERROR = 0
PASS  = 1

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--readFile",default=0,help="Tell the program you want to test reading files x times")
    parser.add_argument("-w","--writeFile",default=0,help="Tell the program you want to test writing files x times")
    parser.add_argument("-z","--size",default=4,help="Tell the program what size files you want in form size1,size2,size3.")
    parser.add_argument("-l","--location",default=os.getcwd(),help="Give us the location of the files")
    parser.add_argument("-L","--remote_location",default="C:\\Users\samsungssd\\Desktop\\",help="Location on computer to read and write files from.\n\n")
    parser.add_argument("-s","--start_serial_port",default="COM13,9600",help="serial COM and port you are using (Separate by comma)\n\t\tex:\tCOM13,9600")
    parser.add_argument("-S","--stop_serial_port",default="COM12,9600",help="serial COM and port you are using (Separate by comma)\n\t\tex:\tCOM12,9600")
    parser.add_argument("-R","--record_time",default=200,help="How long do you want to record")
    parser.add_argument("-c","--create_file",help="give me a size for the file and Ill make it")
    return parser.parse_args()

def time_process(process):
    start = time.time()
    part_1 = process
    part_2 = time.time()-start
    return [part_1,part_2]

def createFile(size,fname):
    try:
        nfile = open(fname,'w')
        for i in range(size*2**10):
            nfile.write(os.urandom(1024))
        nfile.close()
        return PASS
    except:
        return ERROR
    
def removeFile(fname):
    try:
        os.remove(fname)
        return PASS
    except:
        return ERROR

def runProcess(process, pname):
    checkme = time_process(process)
    if checkme[0]:
        err_file.write("Program failed on: "+pname+" in "+str(checkme[1])+" seconds.\n")
    else:
        err_file.write("Successfully ran:  "+pname+" in "+str(checkme[1])+" seconds.\n")

def write_test(size,location,rlocation,start,stop,wait_time):
    #Gen announcements
    sys.stdout.write("Starting write test of "+str(size)+"MB\n")
    sname = str(size)+"MB.txt"
    fname = location+'\\'+sname
    
    #Check to see if file exists
    if os.path.isfile(fname):
        sys.stdout.write("Found "+fname+'\n')
    else:
        sys.stdout.write("Could not find "+fname+".  Created new one.\n")
        runProcess(createFile(size,fname),"createFile("+str(size)+","+fname+")")

    #run program
    sys.stdout.write("Moving file...\n")
    shutil.move(fname,rlocation+'\\'+sname)

    for i in range(wait_time):
        sys.stdout.write('\r'+str(20-i)+' seconds left to start recording\t\t')
        time.sleep(1)
    print()
    
    #start recording
    sys.stdout.write("Start recording...\n")
    start.write(bytes(42)) #what does this do?
    #idle time
    for i in range(wait_time):
        sys.stdout.write("\r"+str(i)+" seconds left till write operation...\t\t")
        time.sleep(1) #is this time to hit the record button?
    print()
    
    #actual thing
    shutil.move(rlocation+'\\'+sname,fname)

    sts.stdout.write("Done\n")
    for i in range(wait_time):
        sys.stdout.write("\r"+str(i)+" seconds left to stop recording\t\t")
        time.sleep(1)
    print()
    stop.write(bytes(42))

    #clear cache
    os.remove(rlocation+'\\'+sname)

def read_test(size,location,rlocation,start,stop,wait_time):
    #Gen announcements
    sys.stdout.write("Starting write test of "+str(size)+"MB\n")
    sname = str(size)+"MB.txt"
    fname = location+'\\'+sname
    
    #Check to see if file exists
    if os.path.isfile(fname):
        sys.stdout.write("Found "+fname+"\n")
    else:
        sys.stdout.write("Could not find "+fname+".  Created new one.\n")
        runProcess(createFile(size,fname),"createFile("+str(size)+","+fname+")")

    #run program
    for i in range(wait_time):
        sys.stdout.write('\r'+str(20-i)+' seconds left to start recording\t\t')
        time.sleep(1)
    print()
    
    #start recording
    sys.stdout.write("Start recording...\n")
    start.write(bytes(42)) #what does this do?
    #idle time
    for i in range(wait_time):
        sys.stdout.write("\r"+str(20-i)+" seconds left till read operation...\t\t")
        time.sleep(1) #is this time to hit the record button?
    print()
        
    #actual thing
    shutil.copy(fname,rlocation+'\\'+sname)

    sys.stdout.write("Done\n")
    for i in range(wait_time):
        sys.stdout.write("\r"+str(20-i)+" seconds left to stop recording\t\t")
        time.sleep(1)
    print()
    stop.write(bytes(42))
    
    #clear cache
    os.remove(rlocation+'\\'+sname)

def main(): #should be only for testing
    start = serial.Serial('COM13',9600)
    stop = serial.Serial('COM12',9600)
    runProcess(read_test(256,os.getcwd(),"C:\\Users\samsungssd\\Desktop\\",start,stop))

if __name__ == '__main__':
    args = parse_input()
    tmp_start = args.start_serial_port.split(',')
    tmp_stop  = args.stop_serial_port.split(',')
    if args.create_file != None:
        createFile(int(args.create_file),args.create_file+"MB.txt")
        quit
    else:
        start = serial.Serial(tmp_start[0],int(tmp_start[1]))
        stop  = serial.Serial(tmp_stop[0],int(tmp_stop[1]))
        sizes = [int(i) for i in args.size.split(',')]
        for size in sizes:
            for i in range(args.readFile):
                runProcess(read_test(size,args.location,args.remote_location,start,stop,args.record_time),'read_test')
            if i in range(args.writeFile):
                runProcess(write_test(size,args.location,args.remote_location,start,stop,args.record_time),'write_test')
                runProcess(createFile(1024,"1024MB"))
                runProcess(removeFile("1024MB"))
    sys.stdout.write("Done\n")

else:
    main()
    a = input("Hit enter to exit")
    
