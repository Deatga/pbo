class year_graduated:
   def __init__(self, year=32):
      self._year = year

   @property
   def Aboutyear(self):
      return self.__year

   @Aboutyear.setter
   def Aboutyear(self, b):
      self.__year = b

grad_obj = year_graduated()
print(grad_obj._year)

grad_obj.year = 2018
print(grad_obj.year)
