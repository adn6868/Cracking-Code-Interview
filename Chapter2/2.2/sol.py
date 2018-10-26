from sys import stdin as I
from sys import stdout as O
from sys import stderr as E
from sys import path as path

path.insert(0, 'C:/Users/anguyen/Desktop/workspace/Cracking-Code-Interview/Chapter2')
from myLinkedList import myLinkedList

def solve(l,remove):
	h = l
	it = l
	for i in range(remove):
		it= it.n
	while it.n != None:
		it = it.n
		h = h.n
	h.n = h.n.n
	return l.toString()


if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		n = I.readline()
		remove = int(I.readline().strip('\n'))	
		l = myLinkedList(None)
		for i in range(int(n)):
			l.addEnd(int(I.readline().strip('\n')))
		O.write("====================\n")
		O.write("Input:  L = "+l.toString()+'\n')
		O.write("Remove element: "+str(remove)+'\n')
		O.write("Output: L = "+ solve(l,remove)+'\n')