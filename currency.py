def fiat_currency_converter(amount, from_currency, to_currency): 
        conversion_rates = {
        ('pkr', 'usd'): 0.0036, 
        ('usd', 'pkr'): 278.0,
        ('eur','pkr'):307.11,
        ('pkr','eur'):0.0033,
        ('aed','pkr'):76.09,
        ('pkr','aed'):0.013,
        ('pkr','pkr'):1,
        }
        if (from_currency, to_currency) in conversion_rates:
                   return amount * conversion_rates[(from_currency, to_currency)]
        else:
                 return "Conversion rate not available."
def crypto_currency_converter(amount, from_currency, to_currency):
        conversion_rates = {
        ('pkr', 'eth'):0.0000014,
        ('eth', 'pkr'):73203.19,
        ('pkr','btc'):0.00,
        ('btc','pkr'):16331063.65,
        ('pkr','not'):0.335689,
        ('not','pkr'):3.04,
        }
        if (from_currency, to_currency) in conversion_rates:
                   return amount * conversion_rates[(from_currency, to_currency)]
        else:
                 return "Conversion rate not available."
print("Enter the currency type you want to change")
print("1 = Fiat Currency")
print("2 = Crypto Currency")
choice = int(input())
amount = float(input("Now type the amount that you want to change: "))
if choice == 1:
     from_currency = input("Now type which fiat currency you wanna change (e.g., pkr): ").lower()
     to_currency = input("Now type the currency name in which you wanna change (e.g., usd): ").lower()
     result = fiat_currency_converter(amount, from_currency, to_currency)
elif choice == 2:
    from_currency = input("Now type which cryptocurrency you wanna change (e.g., ):btc ").lower()
    to_currency = input("Now type the cryptocurrency name in which you wanna change (e.g., eth): ").lower()
    result = crypto_currency_converter(amount, from_currency, to_currency)
else:
   result = "Invalid selection. Please choose either 1 or 2."
print(result)