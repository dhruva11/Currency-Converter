from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal, ROUND_HALF_UP


def convert_currency():
    amount = Decimal(amount_entry.get())
    from_currency = from_combobox.get().upper()
    to_currency = to_combobox.get().upper()

    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)

    currency_codes = CurrencyCodes()
    from_currency_symbol = currency_codes.get_symbol(from_currency)
    to_currency_symbol = currency_codes.get_symbol(to_currency)

    if amount < 10:
        decimal_places = '0.000'
    else:
        decimal_places = '0.00'

    result_textbox.delete(1.0, END)
    result_textbox.insert(END, f"{amount} {from_currency_symbol} = {converted_amount.quantize(Decimal(decimal_places), rounding=ROUND_HALF_UP)} {to_currency_symbol}")


root = Tk()
root.title("Currency Converter")

amount_label = Label(root, text="Amount:")
amount_label.grid(row=0, column=0, pady=10)
amount_entry = Entry(root)
amount_entry.grid(row=0, column=1, pady=10)

from_label = Label(root, text="From:")
from_label.grid(row=1, column=0)
from_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "INR", "AED"])
from_combobox.grid(row=1, column=1)

to_label = Label(root, text="To:")
to_label.grid(row=1, column=2)
to_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "INR", "AED"])
to_combobox.grid(row=1, column=3)

convert_button = Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=0, columnspan=4, pady=10)

result_label = Label(root, text="Converted Amount:")
result_label.grid(row=3, column=0)

result_textbox = Text(root, height=1, width=30)
result_textbox.grid(row=3, column=1, columnspan=3)

root.mainloop()
