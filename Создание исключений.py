class NoneZero(Exception):  # 1
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def div(a, b):
    if b == 0:
        raise NoneZero('деление на ноль невозможно', {'a': a, 'b': b})
    return a / b


try:
    result = div(10, 0)
    print(result)
except NoneZero as e:
    print('Ошибочка вышла')
    print(f'Сообщение об ошибке: {e.message}')
    print(f'Дополнительная информация: {e.extra_info}')

print()


class NameException(Exception):  # 2
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby


def intro(name, hobby):
    if hobby == '':
        raise NameException(f'{name}', 'как это у тебя нет хобби?')
    return name, hobby


try:
    res = intro('Даша', '')
    print(res)
except NameException as e:
    print(f'{e.name}, {e.hobby}')
