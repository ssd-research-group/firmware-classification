#!/usr/bin/env python
from functions import *
from functions import create_file as cfile

def main():
    start   = serial.Serial('COM13',9600)
    stop    = serial.Serial('COM12',9600)
    sizes   = [4,24,64,256,1024]
    floc    = os.getcwd()
    rloc    = "C:\\Users\\samsungssd\\Desktop\\"
    wait    = 20
    test    = ssd_test_class(0,floc,rloc,start,stop,wait)

    trials  = 2
    for size in sizes:
        test.size = size
        test.sname = str(size)+"MB.txt"
        test.fname = test.floc + '\\' + test.sname
        for trial in range(trials):
            test.read_test()
            test.write_test()
            create_file(1024,'1024MB.txt')
            remove_file("1024MB.txt")
    quit()

main()

if __name__ == '__main__':
    args    = parse_input()
    #seed    = args.seed
    temp_start  = args.start_serial_port.split(',')
    temp_stop   = args.stop_serial_port.split(',')
    if args.create_file != None:
        cfile(args.create_file,args.create_file+'MB.txt')
        quit()
    else:
        start   = serial.Serial(temp_start[0],int(temp_start[1]))
        stop    = serial.Serial(temp_stop[0],int(temp_stop[1]))
        tstSSD  = ssd_test_class(0,args.location,args.remote_location,start,stop,args.record_time)
        
        sizes   = [int(i) for i in args.size.split(',')]
        for size in sizes:
            tstSSD.size = size
            for test in range(int(args.readFile)):
                tstSSD.read_test()
            for test in range(int(args.writeFile)):
                tstSSD.write_test()
                create_file(1024,'1024MB.txt')
                remove_file("1024MB.txt")
    
