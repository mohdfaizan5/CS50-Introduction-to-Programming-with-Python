#program which prints the pending amount user has to pay for coke:

# Step1: Assign a variable "due" with amt "50"
due = 50
# Step2: Ask user for int input

import pdb

# Step3: if user enters only 25, 10 or 5 then only subract the amt from pending amt, else keep going
amt_left = True
while amt_left:
    print(f"Amount Due: {due}")
    amt = int(input("Insert Coin: "))
    if amt == 25 or amt == 10 or amt == 5:
        due = due - amt
        # pdb.set_trace()
    # if due < 0:
    if due <= 0:
        due = due.__abs__()
        print(f"Change Owned: {due}")
        break

# Step4: After the pending amt has become 0: exit the program.

