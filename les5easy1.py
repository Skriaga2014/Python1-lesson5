'''
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
'''

import os
import shutil

                                                #КОРОТКИЙ ВАРИАНТ:
#for i in range(1,10): os.mkdir("dir_" + str(i))
#input()
#for i in range(1,10): shutil.rmtree(os.path.join(os.getcwd(), "dir_" + str(i)))

                                                #ПОЛНЫЙ ВАРИАНТ:

a = 0
def povtor(i):
    global a
    if int(a) < 3:
        print("Папка с именем \"{}\" уже имеется. Выберите действие:".format(i))
        print("1 - Пропустить. 11 - Пропукать и не спрашивать больше")
        print("2 - Добавить окончиние _copy. 22 - Добавлять и не спрашивать больше.")
        a = input("Введите значение: ")
        while a != "1" and a != "11" and a != "2" and a != "22":
            a = input("Введено неверное значение. Попробуйте снова: ")
    if a == "1" or a == "11":
        print("Папка \"{}\" не создана, так как уже существует".format(i))
    if a == "2" or a == "22":
        os.mkdir(os.path.join(os.getcwd(), i) + "_copy")
        print("Папка \"{}\" уже существует. Создана папка \"{}\"".format(i, i + "_copy"))


def create(i):
    try:
        os.mkdir(i)
        print("Папка \"{}\" создана".format(i))
    except FileExistsError:
        povtor(i)


def delete(i):
    try:
        shutil.rmtree(os.path.join(os.getcwd(), i))
    except FileNotFoundError:
        print("Папки с именем \"{}\" не существует".format(i))
        return
    print ("Папка \"{}\" удалена".format(i))

if __name__ == "__main__":
    for i in range(1, 10): create("dir_" + str(i))
    input("Нажмите Ввод для продолжения...")
    for i in range(1, 10): delete("dir_" + str(i))