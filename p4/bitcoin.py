#Program that prints the current usd price of bitcoin

import requests, sys, json
from sys import argv

leng_sys = len(sys.argv)
# print(leng_sys)

#PSEDU CODE::
 #1) input should be give through CLI
 #2) If input(argument) cannot be converted to float it must exit with sys.exit() with a error message
 #3) Capture json request from API "https://api.coindesk.com/v1/bpi/currentprice.json", which returns a json object and
        #Where you have to look for current bitcoin price
 #4) Outputs the current cost of \(n\) Bitcoins in USD to four decimal places, using , as a thousands separator.
        #Hint:: print(f"${amount:,.4f}")

def main():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # print(x.text)
    # x = json.load(x)
    x = response.json()
    # print(x["USD"])

	# for result in o["dict_name"]:
	# 	print(result["sub_dict_name"])

    # for result in x["bpi"]:
    #     for _ in result:
    #         print(_["USD"])

    Bitcoin_price = (x["bpi"]["USD"]["rate_float"])
    # print(Bitcoin_price)

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument   ")

    f = sys.argv[1]
    # print(f"arg: {f}")
    if f.isalpha():
        sys.exit("Command-line argument is not a number")
    f = float(f)

    final_price = f * Bitcoin_price
    # final_price = round(final_price)
    print(f"${final_price:,.4f}")

    # p = (f"${final_price:,.4f}")
    # print(p[:-5])

    #fetch live bitcoin price

    #multiply the bit coin price into give input
    # if sys

try:
    ...
    if __name__ == "__main__":
        main()
except requests.RequestException:
    ...
    print("req error")


"""
$ python bitcoin.py
Missing command-line argument
$ python bitcoin.py cat
Command-line argument is not a number
$ python bitcoin.py 1
$38,761.0833
$ python bitcoin.py 1.5
$58,141.6249
$ python bitcoin.py 2
$77,522.1666
$
"""