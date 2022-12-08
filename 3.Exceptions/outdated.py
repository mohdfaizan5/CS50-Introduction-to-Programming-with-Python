#Program that take dates as MM/DD/YYYY and converts it into YYYY/MM/DD format.

# x = "9/8/1636"
# z = "December 80, 1980"
import pdb

user_input = input("Date: ")

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
#S : Take input from user.

    
def method1(x = user_input):
    x = x.split("/")
    if x[1] > 31:
        exit()
    print(f"{x[2]}-{x[0]:02d}-{x[1]:02d}")
    # {i:02d}
        

def method2(z = user_input):
    z = z.replace(",","")
    z = z.split()
    pdb.set_trace()
    # print(type(z[1]))
    # print(z[1])
    # print(type(z[1]))
    mo = int(z[1])
    m1 = 31

    
    if mo > m1:
        exit()
    month = z[0]    #December
    # i = 0
    index = 1
    for _ in MONTHS:
        if month == _:
            z[0] = index # 12
            print(month)
        index += 1
        
    print(f"{z[2]}-{z[0]}-{z[1]}") 
   

try:
    # while True:
        # converting(user_input)
    if user_input[0].isnumeric():
        #If its only date then method1
        method1()

    else:
        #method..
        method2()
        
    
except IndexError:
    print("error")
    # continue
# else:
    # break

#Doubts

# """
# 1. How to convert "1636-9-8" to "1636-09-08" 
#         * How to convert number rounding with 0 in starting
# 1. Why program is stucking during execution.
# ""