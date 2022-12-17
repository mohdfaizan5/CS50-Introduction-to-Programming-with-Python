#Program that take dates as MM/DD/YYYY and converts it into YYYY/MM/DD format.

# x = "9/8/1636"
# z = "December 80, 1980"
import sys


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def method1(x):
    # We are checking if its format is "09/12/1899"
    #   If so then we split the string into list(date,month & year)
    x = x.split("/")

    # We are checking wheather the 
    if int(x[1]) > 31:

        # print("date exceed")
        sys.exit()

    month = int(x[0])
    if month > 13:
        return False

    print(f"{x[2]}-{x[0].zfill(2)}-{x[1].zfill(2)}")
    # print(f"{x[2]}-{x[0]:02}-{x[1]:02}")
    return True

def method2(z):
    z = z.replace(",","")
    z = z.split()
    date= int(z[1])
    fixed_date = 31




    if date> fixed_date:
        return False

        # sys.exit()
    month = z[0]        #December


#some mistake in here
    index = 1          
    for _ in MONTHS:
        if _ == month:
            z[0] = index
            
            print(z[2],end="\n")
            print(z[0].zfill(2))   #these lines are not getting excecuted
            print(date)             #these lines are not getting excecuted
            break                   #these lines are not getting excecuted

        index += 1
    print(f"{z[2]}-{z[0].zfill(2)}-{z[1].zfill(2)}")    #these lines are not getting excecuted
    
    # return True
    # YYYY/MM/DD 
    

while True:
    try:
        user_input = input("Date: ")

        # converting(user_input)
        if user_input[0].isnumeric():

            #If its only date then method1
            method1(user_input)
            break

        else:
            method2(user_input)
            break

    except:
        continue
        # print("error")


#S : Take input from user.










#Doubts

# """
# 1. How to convert "1636-9-8" to "1636-09-08" 
#         * How to convert number rounding with 0 in starting
# 1. Why program is stucking during execution.
# ""



