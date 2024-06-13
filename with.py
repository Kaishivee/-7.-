file_name = 'byron.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    content = file.read()
    print(content)

# Оператор `with` не требует прописывания строки file.closed(),
# т.к. закрывается сразу после выполнения
