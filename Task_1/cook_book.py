def cook_book(new_file, encoding):

    '''Функция считывает файл в указанной кодировке и возвращает словарь 
    с перечиисленными рецептами и ингридиентами. Файл должен быть стандартизирован.'''

    cook_book = {}

    with open(new_file, encoding=encoding) as file:
        for line in file:
            if line != '\n':
                name = line.rstrip('\n')
                cook_book[name] = []
                count = int(file.readline())
                for i in range(count):
                    line = file.readline().rstrip('\n').split(' | ')
                    my_dict = {}
                    my_dict['ingredient_name'] = line[0]
                    my_dict['quantity'] = int(line[1])
                    my_dict['measure'] = line[2]
                    cook_book[name].append(my_dict)
    return cook_book


new_dict = cook_book('file_cook_book.txt', 'utf-8')

for key, value in new_dict.items():
    print(key)
    for new_list in value:
        print(new_list)
