# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Clases.Stamp.Stamper import Stamper
from Clases.Users.ClassMate import ClassMate
import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('E:\\Noel\\Escuela\\UPIITA\\ProyectoTT\\PycharmProjects\\pythonProject1\\Json_New_Account.json')
    us = json.load(file)
    class_mate: ClassMate = ClassMate(us["classmate"])
    stamper: Stamper = Stamper(class_mate, 10, 0)
    stamper.make_signs()
    var = stamper.save_signs()
    print(var)
    print("---------------------")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
