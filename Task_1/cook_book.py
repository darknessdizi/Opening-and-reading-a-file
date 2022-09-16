cook_book = {}

with open('file_cook_book.txt', encoding='utf-8') as file:
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

for i, y in cook_book.items():
    print(i)
    for z in y:
        print(z)
        