import sys
import core
core.work_info('Старт')
instruction = """
                    help - помощь
                    delete - удаление файла или папки
                    create_folder - создание папки
                    create_file - создание файла
                    copy - копирование папки или файла
                    move - перемещение файла или папки
                    rename - переименование файла или папки
                    write - запись информации в файл
                    change_directory - перемещние между папками
                    exit - выход из файлового менеджера
                """
command = sys.argv[1]

if command == 'help':
    print(instruction)
elif command == 'exit':
    print('Работа файлового менеджера завершается!')

elif command == 'delete':
    name = input('Введите имя файла, который хотите удалить: ')
    core.delete_file(name)

elif command == 'copy':
    name = input('Введите имя папки или файла: ')
    new_name = input('Введите новое имя файла: ')
    core.copy_file(name, new_name)

elif command == 'move':
    name = input('Имя файла, который хотите переместить: ')
    new_name = input('Введите название куда хотите переместить: ')
    core.move_or_rename(name, new_name)

elif command == 'rename':
    name = input('Имя файла: ')
    new_name = input('Новое имя файла: ')
    core.move_or_rename(name, new_name)

elif command == 'write':
    name = input('Укажите имя файла: ')
    text = input('Введите текст: ')
    core.write_file(name, text)


elif command == 'create_file':
    name = input('Имя файла: ')
    text = input('Введите текст: ')
    core.create_file(name, text=text)

elif command == 'create_folder':
    name = input('Имя папки: ')
    core.create_folder(name)
elif command == 'list':
    core.get_list()
else:
        print('Команда введена неверно!')
core.work_info('Конец')