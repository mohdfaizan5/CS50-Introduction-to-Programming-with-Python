#Program that tell the user the amt of fuel left in tank, by users input

#Psedu code:
# S1: Takes input from user in form of "x/y" where x and y are int
# S2: Test whether the input is valid: and exeption handling
# S3: Then calculates the round value based on input
#       if input is 3/4 then fuel is 75% = 0.75
#       if input is 2/4 then fuel is 50% = 0.
#       if input is 1/4 then fuel is 25%
#       if input is 4/4 then fuel is F   = 1.0
#       if input is 0/4 then fuel is E   = 0.0
#       if input is 4/0 then fuel is 
#       1.5/3


#S1 and S2
# while True:
#     try:
#         input = input("Fraction: ") 
#         fa = input.split("/")
#         first = int(fa[0])
#         second = int(fa[-1])
#         break
while True:
        try:
            first, second = input("Fraction: ").split("/")
            first = int(first)
            second = int(second)
            # print(first, second)
            answer = first/second * 100
            answer = round(answer)
            # print(answer)
            if answer > 100:
                continue
            # first = int(input[0])
            # print(first)
            # second = int(input[1])
            # print(second)
        # break
        #(ValueError, ZeroDivisionError, IndexError, TypeError):
        except ValueError:
            continue
            print("ValueError")
            
        except ZeroDivisionError:
            continue
            print("ZeroDivisionError")
        
        except:
            continue
            print("other error")
        
        else:
            break

answer = int(answer)
# print(type(answer))
# print(answer)
if answer <= 1.0:
    print("E")
elif answer > 98 and answer < 101:#99 >= answer <= 100:
    print("F")
else:
    print(f"{answer}%")
    # except 
    #     print("error")
    # except ValueError or ZeroDivisionError or TypeError:
    #     print("Retry")
    # else:
    #     break

"""
:) fuel.py exists
:( input of 3/4 yields output of 75%
    expected "75%", not "F\n"
:( input of 1/3 yields output of 33%
    expected "33%", not "F\n"
:( input of 2/3 yields output of 67%
    expected "67%", not "F\n"
:) input of 0/100 yields output of E
:) input of 1/100 yields output of E
:( input of 100/100 yields output of F
    expected "F", not "100%\n"
:) input of 99/100 yields output of F
:) input of 100/0 results in reprompt
:) input of 10/3 results in reprompt
:) input of three/four results in reprompt
:) input of 1.5/4 results in reprompt
:) input of 3/5.5 results in reprompt
:) input of 5-10 results in reprompt
"""