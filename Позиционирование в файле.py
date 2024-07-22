def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'wb') as f:
        for index, string in enumerate(strings, start=1):
            byte_string = string.encode('utf-8')
            byte_position = f.tell()
            f.write(byte_string + b'\n')
            strings_positions[(index, byte_position)] = string

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
