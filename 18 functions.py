import random


def function1() :
           print("hello world")

def function2() :
           print("this is function2")

function1()
function2()

def function3(name):
             print(name)

function3('passing argument')

def function4(*name):
               print("the name is "+name[2])

function4("sahsahnk","rahul","shweta")

# passing list as an argument
namelist=["list",4,4,5,8,4,54]
def function5(name):
         for name in namelist:
                              print(name)

function5(namelist)

