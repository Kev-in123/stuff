class TODO: #creates a class cuz why not

    def __init__(self):
      self.todo = [] #declare the list we're using

    def _add(self, item): 
      self.todo.append(item) 

    def _remove(self, item: str):
      self.todo.pop(self.todo.index(item))

    def _list(self, item = None):
      todo = self.todo
      if not item:
        print("\tTODO\n-----------------------")
        for i in range(len(todo)):
          print(f"{i+1}. {todo[i]}")
        print()
        
      else:
        print(self.todo[item-1])

    def _switch(self, item1, item2):
      self.todo[item1-1], self.todo[item2-1] = self.todo[item2-1], self.todo[item1-1]

t = TODO()
t._add("thing 1")
t._add("thing 2")
t._list()

t._switch(1, 2)
t._list()
