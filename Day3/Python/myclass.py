#!/usr/bin/python

from anotherFile import OtherClass;

class MyClass:
  
  def __init__(self):
     self.x = 10
    
  def printX(self):
     print ("Value of X is " + str(self.x) )

  def setX(self, newValue):
     self.x = newValue

def main():
  myClassObj = MyClass()
  
  print("Initial value of X")
  myClassObj.printX()

  myClassObj.setX(400)

  print("Updated value of X")
  myClassObj.printX()
   
  print ( "From MyClass" )
  print ( __name__ )

  otherObj = OtherClass()
  otherObj.printName()

if __name__ == "__main__":
  main()
