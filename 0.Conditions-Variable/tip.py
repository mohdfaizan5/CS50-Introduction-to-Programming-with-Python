def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent)
    print(f"Leave ${tip:.2f}")
"""
dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
"""

def dollars_to_float(d):
    no_dollar = d.replace("$","")         #why no functions are working here
    d = float(no_dollar)
    return d
"""
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
 remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
"""

def percent_to_float(p):
    no_per = p.replace("%","")
    p = float(no_per)
    p = p * 0.01
    return p

main()
