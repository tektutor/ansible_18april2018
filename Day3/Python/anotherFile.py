class OtherClass:
   def __init__(self):
     print ("OtherClass constructor")

   def printName(self):
      print ( "From OtherClass" )
      print ( __name__ )

if __name__ == "__main__":
   obj = OtherClass()
   obj.printName()
