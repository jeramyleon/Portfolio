# Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.
from dictionaries import states_countries

def tax_calculator(cost, country_or_state):

    try:
        _float = float(cost)
    except ValueError:
        print('You need to enter a number.')
        return False
    cost = float(cost)

    try:
        location = country_or_state.lower()
        category = location[0] 
        tax_rate = states_countries[category][location]
    except KeyError:
        print('State or country not found.')
        return False
    location = country_or_state.lower()
    category = location[0] 
    tax_rate = states_countries[category][location]
    
    tax = cost * tax_rate / 100
    total_cost = cost + tax
    print("Tax: ", tax)
    print("Total Cost with Tax: ", total_cost)

    return True




    


