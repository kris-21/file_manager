import os
import shutil
import datetime

def create_file(name,text = None):
    with open(name,'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть!')

def delete_file(name): # Функция для удаления файлов и папок
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)
def write_file(name,text):
    with open(name,'a', encoding = 'utf-8') as f:
        f.write(text + '\n')

def move_or_rename(name, path):
    try:
        shutil.move(name, path)
    except FileNotFoundError:
        print('Ошибка! Файл не найден!')

def copy_file(name, new_name):
    try:
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
            except FileExistsError:
                print('Error! Folder with this name is existed')
        else:
            shutil.copy(name, new_name)
    except FileNotFoundError:
        print("This file doesn't exist!")

def bounds_check(work_path, new_path):
    if new_path.startswith(work_path):
        return True
    else:
        return False
# Доп.задача - запись работы файлового менеджера в текстовый файл
def work_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt','a',encoding = 'utf-8') as f:
        f.write(result + '\n')
#Доп.задача - список существующих команд
def get_list(working_directory, folders_only=False):
    result = os.listdir(working_directory)
    if folders_only:
        result = list(filter(lambda x: True if os.path.isdir(x) else False, result))
    print(result)

