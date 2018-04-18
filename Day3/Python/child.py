
from parent import Parent;

class Child(Parent):

  def __init__(self):
     Parent.__init__(self)
     print("Child constructor")

  def printDetails(self):
     Parent.publicMethod(self)
#     Parent.__privateMethod(self)

