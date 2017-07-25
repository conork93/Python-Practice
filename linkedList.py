'''
Conor Kennedy
7/25/17


Simple linked list
'''


class Node(object):
  def __init__(self, data, nextNode = None):
    self.data = data
    self.nextNode = nextNode
    
  def get_next (self):
    return self.nextNode
    
  def set_next (self, nextNode):
    self.nextNode = nextNode
    
  def get_data (self):
    return self.data
    
  def set_data (self, data):
    self.data = data
    
class LinkedList (object):
  def __init__(self, root = None):
    self.root = root
    self.size = 0
  def get_size (self):
    return self.size
    
  def add(self, data):
    newNode = Node(data, self.root)
    self.root = newNode
    self.size += 1
    
  def remove(self, data):
    thisNode = self.root
    prevNode = None
    while thisNode:
      if thisNode.get_data() == data:
        if prevNode:
          prevNode.set_next(thisNode.get_next)
        else:
          self.root = thisNode
        self.size -=1
        return True  
      else:
        prevNode = thisNode
        thisNode = thisNode.get_next()
    return False 
    
  def find(self, data):
    thisNode = self.root
    while thisNode:
      if thisNode:
        if thisNode.get_data() == data:
          return data
        else:
          self.root = thisNode.get_next()
    return None
    
mylist = LinkedList()
mylist.add(4)
mylist.add(8)
mylist.add(12)
print("size = "+ str(mylist.get_size()))
mylist.remove(4)
mylist.remove(8)
mylist.remove(12)
print("size = "+ str(mylist.get_size()))
