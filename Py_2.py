from ast import Break
from cgi import print_arguments
import math

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Введите необходимую функцию (+,-,*,/,возведение в степень - ^, логарифм - log)")
    if s == '0':
        break
    if s in ('+', '-', '*', '/', '^', 'log'):
#-------------------------------------------------------------------------
        while True:
            try:
                x = float(input("Введите аргумент x (число): x="))
            except ValueError:
                print("Введенный аргумент не является числом")
                continue
            else:
                break
#-------------------------------------------------------------------------
        while True:
            try:
                y = float(input("Введите аргумент y (число): y="))
            except ValueError:
                print("Введенный аргумент не является числом")
                continue
            else:
                break
#-------------------------------------------------------------------------
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
        elif s == '^':
            print("%.2f" % (x**y))
        elif s == 'log':
            print (math.log(x,y))
    else:
        print("Неверный знак операции!")
