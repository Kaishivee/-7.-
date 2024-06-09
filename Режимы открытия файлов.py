from pprint import pprint

file_name = 'byron.txt'
file = open(file_name, mode='rb')
file.content = file.read()
file.close()
pprint(file.content.decode('utf8'))
