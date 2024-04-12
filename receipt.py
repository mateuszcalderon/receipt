# LAST UPDATE: 04/12/2024.
# Importing datetime library we're able to work with dates and times.
import datetime
# datetime.datetime.now() is designed to return the current UTC date and time.
current_time = datetime.datetime.now()
product_price = float(input("PRICE: "))  # Here the user will enter a price, e.g., 59.00
product_name = input("PRODUCT: ")        # And then a product, e.g., Phone Case
quantity = int(input("QTY: "))           # And finally a quantity, e.g., 1
print("---------------------------")
print()
print("          RECEIPT          ")
# strftime will convert object to a string according to the given format:
# %m shows month as a zero-padded decimal number.
# %d shows day of the month as a zero-padded decimal number.
# %Y shows year with century as a decimal number.
# %H shows hour (24-hour clock) as a zero-padded decimal number.
# %M shows minute as a zero-padded decimal number.
# %S shows second as a zero-padded decimal number.
print(current_time.strftime("%m/%d/%Y.........%H:%M:%S"))
print()
# The .upper() method will return a string where all characters are in upper case.
print(f"PRODUCT   : {product_name.upper()}")
print(f"QTY       : {quantity}")
print()
sub_total = product_price * quantity
print(f"SUB TOTAL : {sub_total:.2f}")
print()
print("7.125% TAX")
tax = 7.125 / 100 * sub_total
print(f"TAX AMOUNT: ${tax:.2f}")
print()
total = tax + sub_total
print(f"TOTAL     : ${total:.2f}")
print()
print("---------------------------")
