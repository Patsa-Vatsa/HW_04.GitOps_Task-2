#Calculator
class Calculator:
  #empty constructor
  def __init__(self):
    pass
  #Accepts two numbers (x1 and x2), returns the sum of these numbers: x1+x2
  def add(self, x1, x2):
    return x1 + x2
  #Accepts two numbers (x1 and x2), returns the product of these numbers: x1?x2
  def multiply(self, x1, x2):
    return x1 * x2
  #Accepts two numbers (x1 and x2), returns the difference between the first and second numbers: x1?x2
  def subtract(self, x1, x2):
    return x1 - x2
  #Accepts two numbers (x1 and x2), returns the difference between the first and second numbers: x1?x2
  def divide(self, x1, x2):
    if x2 != 0:
      return x1/x2
  #Accepts two numbers (x1 and x2), Returns the result of dividing the first number by the second: x1/x12 (if x2 is not equal to 0)