# Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make 
# sure that it is a valid number (look into how credit cards use a checksum).

def credit_card_validator(number):
    try:
        integer = int(number)
    except ValueError:
        print('Non integer value found in input')
        return False
    
    if len(number) != 16: 
        print('Input needs to be 16 digits')
        return False

    credit_card = [int(num) for num in str(number)]
    checking_digit = credit_card.pop()
    credit_card.reverse()
    
    counter = -1
    while counter < 15:
        counter += 1
        if counter % 2 != 0:
            continue
        credit_card[counter] = credit_card[counter] * 2
        if credit_card[counter] > 9:
            credit_card[counter] = credit_card[counter] - 9
    
    result = sum(credit_card)
    result += checking_digit
    if result % 10 != 0:
        return False
    else: 
        return True
    

