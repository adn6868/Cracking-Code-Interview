from sys import stdin as I
from sys import stdout as O
from sys import stderr as E
from sys import path as path

# path.insert(0, 'C:/Users/anguyen/Desktop/workspace/Cracking-Code-Interview/Chapter2')

path.insert(0, 'C:/Users/dorak/Documents/GitHub/Cracking-Code-Interview/Chapter2')
from myLinkedList import myLinkedList

def solve(l1,l2):

	val = l1.d+l2.d
	carry = val // 10
	val = val % 10
	ans = myLinkedList(val)

	while (l1.n != None or l2.n != None):
		if l1.n == None:
			l2 = l2.n
			val = l2.d + carry	
		elif l2.n == None:
			l1 = l1.n
			val = l1.d + carry
		else:
			l1 = l1.n
			l2 = l2.n
			val = l1.d + l2.d + carry
		
		carry = val // 10
		val = val % 10
		# E.write("Carry: "+ str(carry)+ '\n')
		# E.write("Value: "+ str(val)+ '\n')
		# E.write(str(val)+'\n')
		ans.addEnd(val)		
		# E.write("Current Ans: "+ ans.toString()+ '\n')
	if carry!= 0:
		ans.addEnd(carry)

	return ans.toString()
	# return l1.toString() + '\n' + l2.toString() +'\n'

if __name__ == '__main__':
	q = I.readline()
	
	for i in range(int(q)):
		l1 = myLinkedList(0)
		l2 = myLinkedList(0)
		line = I.readline().strip('\n')
		for char in line:
			l1.addEnd(int(char))
		line = I.readline().strip('\n')
		for char in line:
			l2.addEnd(int(char))
		O.write(str(solve(l1,l2))+'\n')
		O.write("=========================\n")
		
