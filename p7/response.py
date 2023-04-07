#PROGRAM THAT TAKES INPUT EMAIL AND RETURN WEATHER THE EMAIL IS "VALID" OR "INVALID"
from validator_collection import validators


def main():
    a = input("What's your email address? ")
    print(validate(a))

def validate(email):
    email_address = validators.email(email)
    # The value of email_address will now be "test@domain.dev"
    if email_address:
        return("Valid")
    else:
        return("Invalid")



try:
    main()
except:
    print("Invalid")
    # Handling logic goes here

# if __name__ == "__main__":
#     main()