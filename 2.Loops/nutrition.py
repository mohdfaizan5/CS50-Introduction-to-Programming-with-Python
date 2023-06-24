#pro

#S1: Take input from user "input"
#S2: Program check wheather the fruit is available
#S3: If available, then prints the amt of calories present in it.

input = input("Fruit name: ").lower()
fruits = {
    'apple':'130',
    'avocado': '50',
    'banana': '110',
    'cantaloupe':'50',
    'grapefruit':"60",
    'grapes':'90',
    'honeydew melon':'50',
    'kiwifruit':'90',
    'lemon':'15',
    'lime':'20',
    'nectarine':'60',
    'orange':"80",
    'peach':'60',
    'pear':'100',
    'pineapple':'50',
    'plums':'70',
    'strawberries':'50',
    'sweet cherries': '100',
    'tangerine': '50',
    'watermelon':'80'
}

if input in fruits:
    print(f"Calories: {fruits[input]}")
else:
    print("")
# print(fruits['apple'])