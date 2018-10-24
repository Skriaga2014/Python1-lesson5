'''
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
'''

import os
print([i for i in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), i))])

                                        #То же, но читабельнее:

#for i in os.listdir(os.getcwd()):                       # Для каждого элемента в текушей папке:
#    element_path = os.path.join(os.getcwd(), i)         # Абсолютный путь к элементу
#    if os.path.isdir(element_path):                     # Если элемент с таким путем является папкой:
#        print(i)                                        # тогда выводим этотэлемент на экран