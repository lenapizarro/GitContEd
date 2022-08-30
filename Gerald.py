#!/usr/bin/env python 3

import platform


class Cow:
    def __init__(self, name, sound, walk, type):   #class constructor: first arg is always self. It makes it a method because it self points at the object
        self._sound = sound  #This notation is used to prevent accessing the class' variable directly
        self._walk = walk
        self._name = name
        self._type = type


    def sound(self):    #self is not a keyword, its a reference to the object
        return self._sound

    def walk(self):
        return self._walk  #getter function 

    def name(self):
        return self._name

    def cowType(self):
        return self._type
    

class Bull: 
    def __init__(self, **kwargs):  #using kwargs so the order of the parameters can be changed 
        self._eat = kwargs['eat'] if 'eat' in kwargs else 'hay'   #ternary operator
        self._rest = kwargs['rest'] if 'rest' in kwargs else '1 hour'
    
    def eat(self):                #getter functions
        return self._eat
    
    def rest(self):
        return self._rest


class Calf:
    def __init__(self, *args): #NOT A GOOD PROGRAMMING PRACTICE TO USE ARGS INSTEAD OF KWARGS, You can get confused on the order of the params if the list is too long
        self._play = args[0] #position in the list
        self._cry = args[1] 

    def play(self, n = None): #Setter-getter function
        if n: 
           self._play = n
        return self._play 
    
    def cry(self):
        return self._cry      

    def __str__(self):  #method to return the characteristics in a print function instead of creating a new function, such as print_Characteristics()
        return 'The calf is {} and {}'.format(self.play(), self.cry())  #we use the methods not the variables we marked as "private/do not touch"

class BabyCow(Cow):
    pass

def print_Characteristics(animal):
    if not isinstance(animal, (Cow, Bull, Calf, BabyCow)):  #checking if the object is instance of classes Cow, Calf and Bull defined here. Using a tuple as an arg 
        raise TypeError('Neither a cow, a calf, a baby calf nor a bull is here!')
    if isinstance(animal, (Cow, BabyCow)): 
        print('The {} is named {} and she says {}. She currently is {}'. format(animal.cowType(), animal.name(), animal.sound(), animal.walk())) 
    if isinstance(animal, Bull):
        print('The bull is eating {} and has rested for {}'. format(animal.eat(), animal.rest()))
    if isinstance(animal, Calf):
        print('The calf is {} and {}'. format(animal.cry(), animal.play()))

 
def main():
    print('we\'ll take a look at our cattle!'.upper())   #String functions 
    newCow = Cow('Lola', 'moo', 'taking a stroll', 'Holstein Friesian')
    cow2 = Cow('Doja Cat', 'moo', 'furiously running', 'British White')
    newBull = Bull(eat= 'grass', rest= '5 hours')
    newBullBilly = Bull()
    newCalf = Calf('playing', 'calm')
    newCalf.play('not playing') #Setter-getter
    cowAge = '48'
    cowAge2 = int(cowAge)  # the int() is actually the integer constructor, because everything in python is an object
    newBabyCow = BabyCow('Lolita', 'moooo', 'running', 'British White')
    print_Characteristics(newCow)
    print_Characteristics(newBull)
    print_Characteristics(cow2)
    print_Characteristics(newBullBilly)
    print_Characteristics(newCalf)
    print_Characteristics(newBabyCow)
    print(newCalf)


if __name__ == '__main__' : main()    #This will return the name of the current module if someone were to import this file