ans = input("What is the Answer of the great Question of life, the Universe And Everything? ").lower().strip()

if ans == "42":
    print("Yes")
elif ans == "forty two":
    print("yes")
elif ans == "forty-two":
    print("yes")
else:
    print("No")