from pprint import pprint

file_name = 'byron.txt'
file = open(file_name, mode='r', encoding='utf8')
file.content = file.read()
file.close()
pprint(file.content)
