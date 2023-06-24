#taking input from user
greet = input("Greeting: ").lower().strip()
# print(greet)

if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h") and greet != "hello": #or greet != "hello ":
    print("$20")

else:
    print("$100")

"""
Hello
Hello, Newman
How you doing?
Whats Happening
"""