import os

def sort_list_file(list_file):
    __list = []
    for file in list_file:
        count = 0
        with open(file, encoding='utf-8') as next_file:
            for i in next_file:
                count += 1
        __list.append((file, count))
        #print(f"Файл: {file} колличество строк {count}")
    return __list

def sort_key(new_list):
    return new_list[1]


list_file = os.listdir()
list_file.remove('final_file.py')

list_file = sort_list_file(list_file)
list_file = sorted(list_file, key=sort_key)

print(list_file)

