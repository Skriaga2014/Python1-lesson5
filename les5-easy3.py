'''
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
'''

from os.path import splitext as split
import shutil

shutil.copyfile(__file__,split(__file__)[0]+"(копия)"+split(__file__)[1])
