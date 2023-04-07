def main():
    fraction = input("Input: ")
    percen = convert(fraction)
    print(gauge(percen))

def convert(fraction):
    first, second = fraction.split("/")
    first = int(first)
    second = int(second)
    # print(first, second)
    answer = first/second * 100
    answer = round(answer)
    # print(answer)
    if answer > 100:
        raise ValueError
    elif second == 0:
        return ZeroDivisionError
    return answer

def gauge(percentage):
    #Telling user low fuel when fuel is less than 1 percent
    percentage = int(percentage)
    if percentage <= 1:
        return "E"

    #Telling fuel is full when feul is greater than 98
    elif percentage > 98 and percentage < 101:#99 >= answer <= 100:
        return "F"

    # Else what percentage is it.
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()