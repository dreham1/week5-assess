



log_file = open("um-server-01.txt") # opens the data file in python




def sales_reports(log_file):#function being initiated
    for line in log_file: #for loop 
        line = line.rstrip() #removes the whitespaces
        day = line[0:3] #sets a day equal to the first characters 
        if day == "Mon":# if day is a specific day
            print(line)  #prints the line


sales_reports(log_file)#prints all of the lines with the specific day
