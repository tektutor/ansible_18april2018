#!/usr/bin/python

def sayHello():
   print("Hello Python!")
   x = 10
   print("Value of X is " + str( x ) )

   print("type of X is", type(x) )
   
   x = "Hello"
   print("type of X is", type(x) )

def add(firstValue, secondValue):
   return firstValue + secondValue

def main():
  sayHello()
  firstNumber = 100
  secondNumber = 200
  result = add ( firstNumber, secondNumber ) 
  print ("The sum of " + str(firstNumber) + " and " + str( secondNumber ) + " is " + str ( result ) )

if __name__ == "__main__":
  main()
