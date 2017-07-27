class Node(object):
  def __init__(self, data, prevNode = None, nextNode = None):
    self.data = data
    self.prevNode = prevNode
    self.nextNode = nextNode
    
  def get_next (self):
    return self.nextNode
    
  def set_next(self, nextNode):
    self.nextNode = nextNode
  
  def get_prev (self):
    return self.prevNode
    
  def set_prev (self, prevNode):
    self.prevNode = prevNode
  
  def get_data (self):
    return self.data
    
  def set_data (self, data):
    self.data = data
    
  def __str__(self):
    return str(self.data)  
    

class DoublyLinkedList(object):
  def __init__(self, root = None):
    self.root = root
    self.size = 0
    
  def get_size(self):
    return self.size
    
  def add (self, data):
    newNode = Node(data, self.root)
    if self.root:
      self.root.set_prev(newNode)
    self.root = newNode
    self.size += 1
    
  def prints (self):
    node = self.root
    while node:
      print (node)
      node = node.get_next()    
    
  def remove(self, data):
    thisNode = self.root
