

# opens the data file in python

log_file = open("um-server-01.txt") 

# loops over file and formats it by day of the week, the date and year, quantity, and product

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)  


sales_reports(log_file)
