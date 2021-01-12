#!/usr/bin/python3
import sys
import re
import numpy as np
import os

def verify_argv() :
    if len(sys.argv) < 3 :
        print("Expecting arguments: option file_name")
        exit(1)
    else:
        options = {"-a","-f","-s","-u","-v"}
        print_ops = sys.argv[1]
        if print_ops not in options:
            print("Option not exist")
            exit(1)
        elif (print_ops == "-u")&(len(sys.argv)<4):
            print("Expecting arguments: -u username file_name")
            exit(1)
        else:
            try:
                open(sys.argv[-1],"r")
            except:
                print("File unreadable")
                exit(1)
            else:
                user_name = sys.argv[2]
                file_to_print = sys.argv[-1]
                return print_ops, user_name, file_to_print

def read_file(file_to_print):
    file_obj = open(file_to_print,"r")
    arr = []
    file_arr = []
    size_arr = []
    user_arr = []
    for line in file_obj:
        linestr = line.replace('\n','').replace('\r','')
        linelist = re.split(',',linestr)
        arr.append(linelist)
        file_arr.append(linelist[0])
        size_arr.append(linelist[1])
        user_arr.append(linelist[2])
    return file_obj, arr, file_arr, size_arr, user_arr
    file_obj.close()

def option_a(file_to_print):
    user_arr = read_file(file_to_print)[4]
    if user_arr == []:
        print("No printing user")
    else:
        filt_arr = list(set(user_arr))
        filt_arr.sort(key=user_arr.index)
        print("Printing users:")
        for x in filt_arr:
            print(x)

def option_f(file_to_print):
    file_arr = read_file(file_to_print)[2]
    print("Total number of files printed:",len(file_arr))

def option_s(file_to_print):
    size_arr = read_file(file_to_print)[3]
    size_sum = 0
    for size in size_arr:
        size_sum += int(size)
    print("Total number of bytes printed:", size_sum)

def option_u(user_name, file_to_print):
    if os.stat(file_to_print).st_size == 0:
        print("Empty file")
    else:
        arr = read_file(file_to_print)[1]
        array = np.array(arr)#2d array
        x, y = np.where(array == user_name)#location indecies 
        if len(x)<1:#no match
            print(user_name,"not found")
            exit(1)
        print("User",user_name,":")
        print("Total  number  of  files  printed:",len(array[x]))
        size_sum = 0
        for size in array[x,y-1]:
            size_sum += int(size)
        print("Total  number  of  bytes  printed:",size_sum)
        print("Largest  file  printed:", np.sort(array[x,y-1])[0])

def option_v():
    print("Student Name: Jiahua Li")
    print("Student ID: 13507912")
    print("Date of completion: 2020/06/01")

def ops_select(print_ops, user_name, file_to_print):
    if print_ops == "-a":
        option_a(file_to_print)
    elif print_ops == "-f":
        option_f(file_to_print)
    elif print_ops == "-s":
        option_s(file_to_print)
    elif print_ops == "-u":
        option_u(user_name, file_to_print)
    elif print_ops == "-v":
        option_v()

# Main section
args = verify_argv()
ops_select(args[0],args[1],args[2])

