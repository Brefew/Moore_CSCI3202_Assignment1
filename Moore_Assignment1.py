#Ian Moore Assignment 1

import Queue

class Queue():
	
	q = Queue.Queue()
	
	def __init__(self):
		pass
		
	def queueSize(self):
		return self.q.queueSize()
	
	def empty(self):
		return self.q.empty()
		
	def put(self, integer):
		self.q.put(integer)
		
	def get(self):
		return self.q.get()

class Stack:
	def __init__(self):
		self.items = []
		
	def push(self, integer):
		self.items.append(integer)
		
	def pop(self):
		return self.items.pop()
		
	def checkSize(self):
		return len(self.items)

class Node():
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None 
		self.parent = None

class BinaryTree():
	
	def __init__(self):
		self.root = None
		
	def add(self, value, parentValue):
		if self.root is None:
			self.root = Node(value)
			print "Node added to tree: ",value
			
		else:
			if not self._add(value, parentValue, self.root):
				print "Parent not found; node not added"
			
	def _add(self, value, parentValue, node):
		if node.key == parentValue:
			if node.left == None:
				node.left = Node(value)
				print "Node added to tree: ",value
				node.left.parent = self.root
				return True
			elif node.right == None:
				node.right = Node(value)
				print "Node added to tree: ",value
				node.right.parent = self.root
				return True
			else:
				print "Parent has two children; node not added"
				return True
				
		else:
			if node.left is not None:
				if node.right is not None:
					return (self._add(value, parentValue, node.left) or self._add(value, parentValue, node.right))
				else:
					return node.left._add(value, parentValue)
			elif node.right != None:
				return node.right._add(value, parentValue)
			else:
				return False
			
			
			
	def delete(self, value):
		if not self._delete(value, self.root):
			print "Node %d not found; could not be deleted" % value
			
	def _delete(self, value, node):
		if node.key == value:
			if node.left is not None or node.right is not None:
				print "Node %d contains children; could not be deleted" % value
				return True
			else:
				if node.parent.left == self:
					node.parent.left = None
					print "Node %d deleted from tree" % value
				else:
					node.parent.right = None
					print "Node %d deleted from tree" % value
				del self
				return True
			
		else:
			if node.left is not None:
				if node.right is not None:
					return (self._delete(value, node.left) or self._delete(value, node.right))
				else:
					return self._delete(value, node.left)
			elif node.right is not None:
				return self._delete(value, node.right)
			else:
				return False
						
					
	def printTree(self):
		if self.root != None:
			self._printTree(self.root)
			
	def _printTree(self, node):
		if node != None:
			print node.key
			self._printTree(node.left)
			self._printTree(node.right)
					

class UnweightedGraph(object):
	vertices = {}
	
	def __init__(self):
		pass 
		
	def addVertex(self,value):
		if value in self.vertices:
			print "Vertex already exists: ", value
		else:
			self.vertices[value] = []
			
	def addEdge(self, value1, value2):
		if value1 == value2:
			print "Edge must connect two different vertices"
		elif not (value1 in self.vertices and value2 in self.vertices):
			print "One or more vertices not found"
		else:
			if value2 in self.vertices[value1]:
				print "Edge already exist between vertices"
			else:
				self.vertices[value1].append(value2)
			
			if value1 in self.vertices[value2]:
				print "Edge already exists between vertices"
			else:
				self.vertices[value2].append(value1)
				
	def findVertex(self, value):
		if value in self.vertices:
			print self.vertices[value]
		else: 
			print "Vertex not found"

	
	
def main():
	
	print "Checking the FIFO Queue: "
	
	q = Queue()
	print "Integers 0-9 inserted in order"
	for i in range(10):
		q.put(i)
	
	print "Integers in order of dequeue:"
	while not q.empty():
		print "Dequeueing: ",q.get()
	
	print "All integers dequeued and queue is deleted"	
	del q
	
	print "\nChecking the integer stack:"
	
	s = Stack()
	
	print "Integers 0-9 are pushed onto the stack."
	for i in range(10):
		s.push(i)
	
	print "The stack size is: ",s.checkSize()	
	
	for i in range(10):
		print "Popping off stack: ", s.pop()
		
	print "All elements popped from stack\n"
	
	print "Now testing Binary Tree:"
	tree = BinaryTree()
	tree.add(1,0)
	tree.add(2,1)
	tree.add(3,1)
	tree.add(4,1)
	tree.add(4,2)
	tree.add(5,2)
	tree.add(6,3)
	tree.add(7,5)
	tree.add(8,5)
	tree.add(9,8)
	tree.add(10,8)
	print "\nTree nodes in pre-order traversal:"
	tree.printTree()
	print "\nNow testing delete method:"
	tree.delete(4)
	tree.delete(5)
	tree.delete(3)
	tree.delete(10)
	tree.printTree()
	
	print "\nNow testing Graph class"
	g = UnweightedGraph()
	print "Adding vertices 0-9 to graph"
	for i in range(10):
		g.addVertex(i)
		print "Adding vertex ",i
	print "\nCreating edges between vertices"
	for i in range(1,10):
		g.addEdge(0,i)
		print "Adding edge (0,%d)" %i
	for i in range(2,10):
		g.addEdge(2, i)
		print "Adding edge (2,%d)" %i
	g.addEdge(4,5)
	g.addEdge(8,10)
	g.addEdge(5,7)
	
	print "Finding adjacent vertexes"
	g.findVertex(0)
	print "Adjacent vertices of 0"
	g.findVertex(1)
	print "Adjacent vertices of 1"
	g.findVertex(2)
	print "Adjacent vertices of 2"
	g.findVertex(3)
	print "Adjacent vertices of 3"
	g.findVertex(7)
	print "Adjacent vertices of 7"
	
	
	
if  __name__ =='__main__':main()
