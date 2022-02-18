log_file = open("um-server-01.txt")  #open file um-server-01.txt and return as a file object.


def sales_reports(log_file):    # def keyword is to define a function. In this case, it  defines the function sales_reports(parameter).

    for line in log_file:       #for...in loop is used to walk through each line of the file.
        line = line.rstrip()    #rstrip() method is used to remove any trailing spaces.
        day = line[0:3]         #this method is to get the first three letters (from index 0 to 2) of a string
        if day == "Tue":        #if statement to check if "day" equals "Tue".
            print(line)         #print out the line contains "Tue" to the screen.


sales_reports(log_file)         #invoke the function and pass in the "log_file" as its parameter
log_file.seek(0)

def over_ten_melons(file):
    for line in file:
        line = line.split()
        if int(line[2]) >10:
            print(' '.join(line))

over_ten_melons(log_file)

log_file.close()