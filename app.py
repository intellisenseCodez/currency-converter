
# This program will be able to convert from one currency to another.
import converter as conv


msg = """
Welcome to our currency converter app.

Amount (NGN): # {user_amount}
Amount ({to_currency}): $ {amount_in_currency}


"""

amount_in_naira = input("Enter amount (NGN): ")
to_currency = input("Convert to:\n 1. USD \n 2. EUR\n 3. YEN\n 4. RAND\n 5. RUPEE: ")

# conditions
if to_currency == '1':
    to_value_USD = conv.convert_to_USD(from_value=amount_in_naira)
    print(msg.format(user_amount=amount_in_naira,to_currency='USD', amount_in_currency=to_value_USD))
elif to_currency == '2':
    to_value_EUR = conv.convert_to_EUR(from_value=amount_in_naira)
    print(msg.format(user_amount=amount_in_naira,to_currency='EUR', amount_in_currency=to_value_EUR))
elif to_currency == '3':
    to_value_YEN = conv.convert_to_YEN(from_value=amount_in_naira)
    print(msg.format(user_amount=amount_in_naira,to_currency='YEN', amount_in_currency=to_value_YEN))
elif to_currency == '4':
    to_value_RAND = conv.convert_to_RAND(from_value=amount_in_naira)
    print(msg.format(user_amount=amount_in_naira,to_currency='RAND', amount_in_currency=to_value_RAND))
elif to_currency == '5':
    to_value_RUPEE = conv.convert_to_RUPEE(from_value=amount_in_naira)
    print(msg.format(user_amount=amount_in_naira,to_currency='RUPEE', amount_in_currency=to_value_RUPEE))
else:
    print("Invalid Input")


