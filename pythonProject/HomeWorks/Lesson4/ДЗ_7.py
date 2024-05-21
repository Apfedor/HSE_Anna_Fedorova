'''
Реализуйте класс CourtCase.
При вызове метода конструктора экземпляра (__init__) должны создаваться следующие атрибуты экземпляра:
● case_number (строка с номером дела — обязательный параметр) передаётся в качестве аргумента при создании экземпляра
● case_participants (список по умолчанию пустой)
● listening_datetimes (список по умолчанию пустой)
● is_finished (значение по умолчанию False)
● verdict (строка по умолчанию пустая)

У экземпляра должны быть следующие методы:
● set_a_listening_datetime — добавляет в список listening_datetimes судебное
заседание (структуру можете придумать сами)
● add_participant — добавляет участника в список case_participants (можно просто
ИНН)
● remove_participant — убирает участника из списка case_participants
● make_a_decision — вынести решение по делу, добавить verdict и сменить
атрибут is_finished на True
'''

from datetime import datetime


class CourtCase():
    __listening_datetimes = []
    __case_participants = []

    def __init__(self, case_number: str, case_participants=None, listening_datetimes: str = None):
        self.is_finished = False
        self.verdict = ''
        if case_number == '':  # строка с номером дела — обязательный параметр
            self.case_number: str = f'№{input('Введите номер дела: ')}'
        else:
            self.case_number = case_number
        if case_participants is not None:
            self.add_participant(case_participants)
        if listening_datetimes is not None:
            self.set_a_listening_datetime(listening_datetimes)
        # print('ini> ', self.case_number, self.listening_datetimes, self.case_participants, f'Вердикт: "{self.verdict}"',
        #       self.is_finished)

    @classmethod
    def set_a_listening_datetime(cls, value=None):  # добавляет в список listening_datetimes судебное
        if value is None:
            value: str = input('Введите дату и время заседания в формате дд.мм.гггг чч:мм: ')
            value: datetime = datetime.strptime(value, '%d.%m.%Y %H:%M')
        else:
            value = datetime.strptime(value, '%d.%m.%Y %H:%M')
        cls.__listening_datetimes.append(str(value))

    @property
    def listening_datetimes(self):
        return self.__listening_datetimes

    @property
    def case_participants(self):
        return self.__case_participants

    @classmethod
    def add_participant(cls, value=None):  # добавляет участника в список case_participants (можно просто ИНН)
        if value is None:
            value = input('Введите ИНН участника: ')
        elif isinstance(value, list):
            cls.__case_participants.extend(value)
            return
        cls.__case_participants.append(value)

    @classmethod
    def remove_participant(cls, value: str = None):  # убирает участника из списка case_participants
        if value == '':
            print('Введены некорректные данные практиканта')
            return False
        if value in cls.__case_participants:
            cls.__case_participants.remove(value)
        else:
            value = input(f'Введите ИНН практиканта для удаления: {cls.__case_participants}: ')
            cls.remove_participant(value)

    def make_a_decision(self,
                        value: str):  # вынести решение по делу, добавить verdict и сменить атрибут is_finished на True
        self.verdict = value
        self.is_finished = True


def main():
    a = CourtCase('№12/3', ['1234567890', '1234567891'], '12.09.2024 15:10')
    print('ini> ', a.case_number, a.listening_datetimes, a.case_participants, f'Вердикт: "{a.verdict}"', f'Завершен: "{a.is_finished}"')
    a.add_participant('0987654321')
    a.add_participant('0111111111')
    a.remove_participant('1234567890')
    a.set_a_listening_datetime('12.11.2024 12:11')
    a.set_a_listening_datetime('13.11.2024 13:15')
    a.make_a_decision('Виновен!')
    print('stop>', a.case_number, a.listening_datetimes, a.case_participants, f'Вердикт: "{a.verdict}"', f'Завершен: "{a.is_finished}"')
    pass


main()
