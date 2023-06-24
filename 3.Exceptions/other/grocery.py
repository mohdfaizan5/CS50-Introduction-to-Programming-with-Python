all_items = {}
user_items = []



def count_items(all_items):
    user_items.sort()

    for item in user_items:
        if item not in all_items:
            all_items[item] = 1

        else:
            all_items[item] += 1



def main(all_items, user_items): #=all_items, user_items=user_items):
    # i = 0
    while True:
        items = input("").upper()
        user_items.append(items)




try:
    main(all_items,user_items)
except EOFError:
    count_items(all_items=all_items)
    # print("EOF error")
    # print(f"final: {all_items}")
    for _ in all_items:
        i = 0
        print(f"{all_items[_]} {_}")
        i += 1