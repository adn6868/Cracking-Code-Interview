from SetOfStack import *

def testSetOfStack1():
	s = SetOfStack(4)
	l= [1,2,3,4,5,6,7,8,9,10,11]
	for i in l:
		s.add(i)
	for i in s.setOfStack:
		print(i.toString())
	for i in range(len(l)):
		print(s.pop())
def testSetofStack2():
	s = SetOfStack(4)
	l = [1,2,3,4,5,6,7,8,9]
	for i in l:
		s.add(i)
	print(s.toString())
	print(s.pop())
	print(s.toString())
	print(s.pop())
	print(s.toString())
	s.add(10)
	print("add 10")
	print(s.toString())
	print(s.pop())
	print(s.toString())
	s.add(11)
	print("add 11")
	print(s.toString())

	s.add(11)
	print("add 11")
	print(s.toString())
	s.add(11)
	print("add 11")
	print(s.toString())

	print(s.pop())
	print(s.toString())
	print(s.pop())
	print(s.toString())

	print("pop stack at 1st position")
	print(s.popAt(0))
	print(s.toString())

def testStack():
	s = Stack()
	l = [1,2,3,4,5,6,7]
	for i in l:
		s.add(i)
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.toString())
	print(s.pop())
if __name__ == '__main__':
	testSetofStack2()