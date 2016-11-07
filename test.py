#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-
#  my first code
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(my):
    my.run()
    my.run()

a = Animal()
d = Dog()
c = Cat()


if(isinstance(c,Animal)):
    print("c is a Dog class")
else:
    print("c is not a Dog class")
