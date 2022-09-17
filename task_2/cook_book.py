def cook_book(new_file, encoding):

    '''Функция считывает файл в указанной кодировке и возвращает 
    
    словарь с перечиисленными рецептами и ингридиентами. Файл должен
    
    быть стандартизирован.
    
    '''

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

def get_shop_list_by_dishes(dishes, person_count):

    '''Функция на входе получает список блюд и колличество персон. 
    
    Возвращает словарь всех ингридиентов и их колличество необходимое
    
    для приготовления блюд из списка.
    
    '''

    ingredients = {}
    __cook_book = cook_book(FILE, ENCODING)
    for name in dishes:
        if name in __cook_book:
            for element in __cook_book[name]:
                if element.get('ingredient_name') in ingredients:
                    dict_ingridient = ingredients[element.get('ingredient_name')]
                    dict_ingridient['quantity'] += (
                        element.get('quantity') * person_count
                        )
                else:
                    ingredients[element.get('ingredient_name')] = (
                        {'measure': element.get('measure'), 
                        'quantity': element.get('quantity') * person_count}
                        )
    return ingredients


ENCODING = 'utf-8'
FILE = 'file_cook_book.txt'

list_dishes = ['Запеченный картофель', 'Омлет']
number_of_ingredients = get_shop_list_by_dishes(list_dishes, 2)

for key, value in number_of_ingredients.items():
     print(key, value)

print('\n', number_of_ingredients)
     
