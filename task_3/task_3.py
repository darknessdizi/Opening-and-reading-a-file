import os


def sort_list_file(list_file):

    '''Функция принимает список файлов. Считывает их и возвращает список
    
    кортежей содержащих имя файла и колличество строк в нем.
    
    '''
    __list = []
    for file in list_file:
        count = 0
        with open(file, encoding='utf-8') as next_file:
            for i in next_file:
                count += 1
        __list.append((file, count))
    return __list

def sort_key(new_list):

    '''Функция для сортировки кортежей по колличеству строк'''

    return new_list[1]

def open_file(list_file):

    '''Функция получает отсортированный список кортежей содержащих имя
    
     файла и колличество строк в нем. Файлы по списку считываются и 

     записываются в новый файл.
    
    '''

    for file in list_file:
        file_mode = chek_file()
        with open(file[0], 'r', encoding='utf-8') as f_read, \
        open('final_file.txt', file_mode, encoding='utf-8') as f_write:
            text_file = file[0] + '\n' + str(file[1]) + '\n'
            f_write.write(text_file)
            count = 0
            for text_file in f_read:
                count += 1
                number = file[0].rstrip('.txt')
                text_file = f'Строка номер {count} файла номер {number} ' + text_file
                f_write.write(text_file)
            f_write.write('\n')

def chek_file():

    '''Функция проверяет наличие файла в текущем каталоге. Если файла нет,
    
    то назначется режим для записи "w", если файл существует, тогда 
    
    назначается режим "а"
    
    '''

    if 'final_file.txt' in os.listdir():
        file_mode = 'a'
    else:
        file_mode = 'w'
    return file_mode


list_file = os.listdir()
list_file.remove('task_3.py')

if 'final_file.txt' in os.listdir():
    list_file.remove('final_file.txt')

list_file = sort_list_file(list_file)
list_file = sorted(list_file, key=sort_key)

open_file(list_file)