from funcs import *

data = open_file('data_transactions.json')
sorted_data = sorted_executed(data)

for i in sorted_data:
    print(f"\n{formatted_date(i)} {get_description(i)}")
    print(f"{get_sender(i)} -> {get_recipient(i)}")
    print(f"{get_transfer_amount(i)} {get_currency(i)}")
