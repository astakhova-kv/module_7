def custom_write(file_name, strings):
    name = file_name
    file = open(name, 'a', encoding='utf-8')
    keys = []
    for i in range(len(strings)):
        keys.append((i+1,int(file.tell())))
        file.write(strings[i])
        file.write('\n')
    values = []
    for i in strings:
        values.append(i)
    strings_positions = dict(zip(keys, values))
    file.close()
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
