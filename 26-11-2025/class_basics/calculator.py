class Calculator:
  def __init__(self, x, y):
    self.x=x
    self.y=y

  def add(self):
    return self.x + self.y
  
  def sub(self):
    return self.x - self.y
  
  def mult(self):
    return self.x * self.y
  
  def div(self):
    if self.y == 0:
      raise ZeroDivisionError("Cannot divide by zero")
    return self.x / self.y

c = Calculator(int(input()),int(input()))
print("Addition:", c.add())
print("Subtraction:", c.sub())
print("Multiplication:", c.mult())
print("Division:", c.div())
