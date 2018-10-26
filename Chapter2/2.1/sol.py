from sys import stdin as I
from sys import stdout as O
from sys import stderr as E
from sys import path as path

path.insert(0, 'C:/Users/anguyen/Desktop/workspace/Cracking-Code-Interview/Chapter2')
from myLinkedList import myLinkedList

# def solve(l):
# 	if l.d == None:
# 		return "bro, wtf"
# 	it1 = l
# 	it2 = l.n
# 	while it2 != None:
# 		runner = it1
# 		while runner != None:
# 			if runner.d == it2.d:
# 				tmp = it2.n;
# 				it1.n = tmp
# 				it2 = tmp
# 				l.delete(runner.d)
# 				break
# 			runner = runner.n
# 		if runner == it2:
# 			it1 = it2
# 			it2 = it2.n
# 	return l.toString()
	# E.write(n)
def solve(l):
	it = l
	adict ={}
	while it.n != None:
		if it.d in adict.keys():
			l.delete(it.d)
		else:
			adict[it.d] = True
		it = it.n
	return l.toString()


if __name__ == '__main__':
	q = I.readline()
	l = myLinkedList(0)
	for i in range(int(q)):
		l.addEnd(int(I.readline()))
	O.write("Input:  L = "+l.toString()+'\n')
	O.write("Output: L = "+ solve(l)+'\n')