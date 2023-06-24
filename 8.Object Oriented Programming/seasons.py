import datetime, inflect, re , pyfiglet
import sys
from datetime import date

p = inflect.engine()
# # 365 days in a year, there are minutes in that same year it depends on how many of those are leap years with 366
# days In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years
# there have been since! There is an algorithm for such , but let’s not reinvent that wheel. Let’s use a library
# instead. Fortunately, Python comes with a datetime module that has a class called date


# S2: prints how old they are in minutes, rounded to the nearest integer,
#       using English words instead of numerals, without any and between words.
# S3: that the user was born at midnight (i.e., 00:00:00) on that date. current time is
#     also midnight.
# even if the user runs the program at noon, assume that it’s actually midnight,
# on the same date. Use datetime.date.today to get today’s date, per

def main():

    # S1: prompts the user for their date of birth in YYYY-MM-DD format
    usr = input("Date of Birth: ")
    try:
        print(convert(usr))
    except:
        sys.exit("Invalid date")



def convert(usr):

    # print("convert is called")
    # checking weather the given date by user is true:
    if re.search("^[0-9]{4}-(([0-9]){2}|10|11|12)-(([0-2][0-9])|30|31)$", usr):
        year, month, date = usr.split("-")
        date_of_birth = datetime.date(int(year), int(month), int(date))
        # print(date_of_birth)
        date_today = datetime.date.today()
        diff = date_today - date_of_birth
        # print(diff)
        minutes = diff.days * 24 * 60
        # print(minutes)
        out_put = p.number_to_words(minutes, andword="")
        out_put = (f'{out_put.capitalize()} minutes')
        # print(out_put)
        return out_put
    else:
        raise ValueError


# def something(date_today, date_of_birth):
#
#     return diff


#You’re welcome to import other (built-in) libraries.
  # Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.
  # Ensure that your program will not raise any exceptions.



if __name__ == "__main__":
    main()