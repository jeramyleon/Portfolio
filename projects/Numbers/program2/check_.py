from ccard_validator import credit_card_validator

user_input = input("Enter a credit card number: ")
if credit_card_validator(user_input):
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")