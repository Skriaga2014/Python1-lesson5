'''
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
'''

import os
from os.path import splitext as split
import sys
from shutil import copyfile as copy


print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def cp_def():
    print("cp <file_name> - создает копию указанного файла")
    try:
        copy(dir_name, split(dir_name)[0] + "(copy)" + split(dir_name)[1])
        print("Создана копия файла {} под именем {}".format(dir_name, split(dir_name)[0] + "(copy)" + split(dir_name)[1]))
    except FileNotFoundError:
        print("Файл с таким именем не найден")
    except TypeError:
        print("Не введено имя файла")

def rm_def():
    print("rm <file_name> - удаляет указанный файл")
    q = input("Вы уверены, что хотите удалить {}? y/n:".format(dir_name))
    while q != "y" and q != "n":
        print("Введено неверное значение.")
        q = input("Вы уверены, что хотите удалить {}? y/n:".format(dir_name))
    if q == "y":
        try:
            os.remove(dir_name)
            print("Файл {} удален".format(dir_name))
        except FileNotFoundError:
            print("Файл с таким именем не найден")
    else:
        print("Операция отменена пользователем")
        return

def cd_def():
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    try:
        os.chdir(dir_name)
        print("Текущей директорией стала {}:".format(dir_name))
        print("os.getcwd() =", os.getcwd())
    except FileNotFoundError:
        q = input("Директории {} не существует. Создать? y/n:".format(dir_name))
        while q != "y" and q != "n":
            print("Введено неверное значение.")
            q = input("Создать директорию {}? y/n:".format(dir_name))
        if q == "y":
            os.mkdir(dir_name)
            print("Создана директория", dir_name)
            os.chdir(dir_name)
            print("Текущая директория (os.getcwd()):", os.getcwd())
        else:
            print("Операция отменена пользователем")
            return

def ls_def():
    print("ls - отображение полного пути текущей директории")
    print("Текущая директория:", os.getcwd())

do = {
    "help": print_help,
    "cp": cp_def,
    "rm": rm_def,
    "cd": cd_def,
    "ls": ls_def,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")