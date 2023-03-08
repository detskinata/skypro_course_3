import json
from datetime import date


def open_file(file_json):
    with open(file_json, encoding='UTF-8') as file:
        data_json = json.load(file)
        return data_json


def sorted_executed(data_json):
    sorted_list = []
    for i in data_json:
        if i == {}:
            continue
        if i['state'] == "EXECUTED":
            sorted_list.append(i)
    sorted_list.sort(key=lambda dictionary: dictionary['date'], reverse=True)
    return sorted_list[:5]


def formatted_date(transaction_data):
    date_operation = transaction_data.get('date')
    index = date_operation.index('T')
    date_operation = list(map(int, date_operation[0:index].split('-')))
    the_date = date(date_operation[0], date_operation[1], date_operation[2])
    return the_date.strftime("%d.%m.%Y")


def get_description(transaction_data):
    description = transaction_data.get('description')
    return description


def get_sender(transaction_data):
    sender = transaction_data.get('from')
    if sender == None:
        return f"Данные об отправителе отсутствуют"
    else:
        sender = sender.split()
        return f"{' '.join(sender[:-1])} {sender[-1][:4]} {sender[-1][0:2]}** **** {sender[-1][-4:]}"


def get_recipient(transaction_data):
    recipient = transaction_data.get("to")
    return f"Данные о получателе отсутствуют" if recipient == None else f"{' '.join(recipient.split()[:-1])} **{recipient[-4:]}"


def get_transfer_amount(transaction_data):
    transfer_amount = transaction_data['operationAmount'].get("amount")
    return transfer_amount


def get_currency(transaction_data):
    currency = transaction_data['operationAmount']['currency'].get('name')
    return currency



