# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
from functools import wraps
class dec_singleton(type):
  instance = {}
  def __call__(cls, *args, **kwargs):
    print(id(cls))
    if cls not in dec_singleton.instance:
      dec_singleton.instance[cls] = super(dec_singleton,cls).__call__(*args, **kwargs)
    return dec_singleton.instance[cls]
class Func(metaclass=dec_singleton):
  def __init__(self,x):
    self.y = x
    print("Called init somehow ", x)
    pass
  def call(self):
    print("Calling called ", self.y)
print(id(Func))
obj1 = Func(30)
obj2 = Func(40)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
