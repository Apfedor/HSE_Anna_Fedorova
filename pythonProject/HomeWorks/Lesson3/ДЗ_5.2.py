"""
2. Напишите регулярное выражение для поиска email-адресов в тексте.
"""

import json
import re

_file_name_: str = '10000_efrsb_messages.json'


def Example_dz5_2():
    mail_dict = {}
    with open(_file_name_, 'r') as f:
        efrsb: tuple = json.load(f)  # реестр банкротов в виде кортежа из словарей
        for i in efrsb:
            temp = search_email(i)
            if temp:
                mail_dict.update({i['publisher_inn']: list(set(temp))})
    with open('emails.json', 'w') as f:
        json.dump(mail_dict, f)

    print(mail_dict)
    pass


def search_email(self: dict) -> list:
    mail_pattern = re.compile(r'\b[0-9a-zA-Z.-_-]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')
    s: str = self['msg_text']
    # s = s.replace('/', ' ')
    s = s.replace(':', ' ')
    return re.findall(mail_pattern, s)


Example_dz5_2()
