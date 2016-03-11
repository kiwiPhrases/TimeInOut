import time
import os
from datetime import datetime
"""
################################################################################
INPUT:
    NONE
OUTPUT:
    1. day_times.txt
#################################################################################
DESCRIPTION:
    Designed to keep track of time away from the working table(table includes
    meetings and shared Bloomberg terminal). 
    
    Record time stamps of times away at the office:
        1. Program starts, records time in at office.
        2. User supplies breaks and reason
        3. If "out of office" supplied then program records final time, 
            calculates total time at table, exits(). 
    ##process: get start and end time, calculate the differential
                -substract other time differentials to get total time in.
#################################################################################
"""
def write_to_file(String,  file_name = "day_times.txt"):
    file_exists = os.path.isfile(file_name)
    
    if file_exists is False:
        with open("day_times.txt", "w") as f:
            f.write(String)
        print("\nFile did not exist, wrote data to new file: [%s]" %file_name)
        
    if file_exists:
        with open("day_times.txt", "a") as f:
            f.write(String)
        #print("\nData written to file: [%s]" %file_name)
    return()
    
def start_day(option_list):
    temp_time = time.localtime()
    #Record current date
    startDate =  "/".join([str(t) for t in temp_time[:3]])
    
    #Record current time
    startTime = ":".join([str(t) for t in temp_time[3:6]])
    
    #Put into a single string
    String = "".join(["\n"+"--"*15,"\n"+str.title(option_list[0]),
        "\n\tDate: %s" %startDate, "\n\tTime: (%s)" %startTime])
    
    #write to file
    write_to_file(String)
    
    #return start_time
    return(temp_time[3:6])
    
def get_user_selection(option_list):

    ##print options:
    print("\n".join([str(item) for item in enumerate(option_list)]))
    
    ##request user input:
    usr_input = 10^5
    while (usr_input >= len(option_list)):
        try:
            usr_input = int(input("\nPlease choose one of above options: "))
        except ValueError:
            "\nPlease make sure to enter an integer!"
            usr_input = int(input("\nPlease choose one of above options: "))
        if option_list[usr_input] == "custom":
            usr_selection=input("\nPlease enter reason for parting with your desk: ")
        else:
            usr_selection = option_list[usr_input]
    return(usr_selection)
   
def enter_user_back():
    ##re-admit the user
    usr_input = "chairs"
    while usr_input != "":
        usr_input = input("\n\tBack? Press [:Enter:] ")
    Time = process_user_selection("  Back")
    return(Time)
    
def process_user_selection(usr_selection):
    raw_time = time.localtime()[3:6]
    Time = ":".join([str(t) for t in raw_time])
    String = "\n\t-%s: %s" %(str.title(usr_selection), Time)
    write_to_file(String)
    return(Time)
 
def get_time_diff(time_in, time_out):
    #time_diffs=tuple([x-y for x,y in zip(time_out, time_in)])
    t1 = datetime.strptime(time_in, "%H:%M:%S")
    t2 = datetime.strptime(time_out, "%H:%M:%S")
    time_diff = t2-t1
    return(time_diff)
    
def main():
    os.chdir("c:/users/spiffyapple/Desktop")
    option_list = ["in at office", "out of office",
        "at the loo", "grabbed a beverage", "at lunch", "peeled a clementine", "peeled a banana", "custom"]
    ##initiates program for the day by writing "In at Office: time and date"
    start_time = start_day(option_list)
    print("--"*20)
    print("--"*20)
    print("\nYou're now in the office\n")
    
    ##loop until user selects "out of office"
    usr_input = "artichokes"
    time_diff_list=[]
    
    ##Keep a query up while in office
    while usr_input != "out of office":
        usr_input = get_user_selection(option_list)
        if usr_input != "out of office":
            time_out = process_user_selection(usr_input)
            time_in = enter_user_back()
            time_diff_list.append(get_time_diff(time_out, time_in))
        if usr_input == "out of office":
            end_time = process_user_selection("out of office")
    print("Day ended, ciao!")
    
    ##Get total time between in of office and out of office.
    total_time = get_time_diff(":".join([str(t) for t in start_time]), end_time)
    
    ##substract time away from desk
    for d in time_diff_list:
        net_time = total_time - d
    
    hours, remainder = divmod(net_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    endString = "\n\t\tNet time for day: [%s]" %":".join([str(t) for t in [hours, minutes, seconds]])
    
    ##write final day net_time to file
    with open("day_times.txt", "a") as f:
        f.write(endString)
    
if "__main__"==__name__:
    main()  