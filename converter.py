
# exchange rate
NGN_to_USD = 440.80
NGN_to_EUR = 464.37
NGN_to_YEN = 3.30
NGN_to_RAND = 25.40
NGN_to_RUPEE = 5.43

def convert_to_USD(from_value):
    amount_in_dollar = float(from_value) * NGN_to_USD
    return amount_in_dollar


def convert_to_EUR(from_value):
    amount_in_euro = float(from_value) * NGN_to_EUR
    return amount_in_euro

def convert_to_YEN(from_value):
    amount_in_yen = float(from_value) * NGN_to_YEN
    return amount_in_yen

def convert_to_RAND(from_value):
    amount_in_rand = float(from_value) * NGN_to_RAND
    return amount_in_rand

def convert_to_RUPEE(from_value):
    amount_in_rupee = float(from_value) * NGN_to_RUPEE
    return amount_in_rupee




#Task YEN, RAND, RUPEE