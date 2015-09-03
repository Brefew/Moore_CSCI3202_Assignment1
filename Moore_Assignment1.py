#Ian Moore Assignment 1

import Queue

q = Queue.Queue()

class Stack:
	def __init__(self):
		self.items = []
		
	def push(self, integer):
		self.items.append(integer)
		
	def pop(self):
		return self.items.pop()
		
	def checkSize(self):
		return len(self.items)

	
def main():
	
	print "Checking the FIFO Queue: "
	
	print "Integers 0-9 are added to the Queue in order."
	for i in range(10):
		q.put(i)
		
	while not q.empty():
		print "Dequeuing: ", q.get(i)
		
	print "All elements dequeued.\n"
	
	print "Checking the integer stack:"
	
	s = Stack()
	
	print "Integers 0-9 are pushed onto the stack."
	for i in range(10):
		s.push(i)
	
	print "The stack size is: ",s.checkSize()	
	
	for i in range(10):
		print "Popping off stack: ", s.pop()
		
	print "All elements popped from stack"
	
if  __name__ =='__main__':main()
