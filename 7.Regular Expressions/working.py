import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if pattern := re.search(r"(\d{1,2}):?(\d{2})? ([A|P]M) to (\d{1,2}):?(\d{2})? ([A|P]M)",s):
    # if pattern := re.search(r"^([0-9]|[0-1][0-2])\:?([0-5][0-9])? ([A|P]M) to ([0-9]|[0-1][0-2])\:?([0-5][0-9])? ([A|P]M)$",s):
        # print("YEs")
        h1,m1,am_pm1,h2,m2,am_pm2 = pattern.group(1),pattern.group(2),pattern.group(3),pattern.group(4),pattern.group(5),pattern.group(6)

        if m1:
            if int(m1) >= 60:
                raise ValueError
        if m2:
            if int(m2) > 60:
                raise ValueError
        h1 = int(h1)
        if am_pm1 == "PM" and h1 != 12:
            h1 += 12
        elif am_pm1 == "AM" and h1 == 12:
            h1 -= 12

        #If only normal hours are given
        if m1 == None:
            time1 = (f"{h1:02}:00")
        else:
            time1 = (f"{h1:02}:{m1}")

        h2 = int(h2)
        if am_pm2 == "PM" and h2 != 12:
            h2 += 12
        elif am_pm2 == "AM" and h2 == 12:
            h2 -= 12

        #If only normal hours are given
        if m2 == None:
            time2 = (f"{h2:02}:00")
        else:
            time2 = (f"{h2:02}:{m2}")

        #return time in 24hour format
        time = f"{time1} to {time2}"
        # print(time)
        return time
    else:
        raise ValueError

# try:
#     main()

# except:
#     print("error")

if __name__ == "__main__":
    main()