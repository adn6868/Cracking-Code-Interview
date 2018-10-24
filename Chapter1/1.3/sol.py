from sys import stdin as I
from sys import stdout as O
from sys import stderr as E


def solve(n):
	li =[]
	char =0
	while char < len(n):
		if n[char] not in li:
			li.append(n[char])		
		else:
			n = n.replace(n[char],'',1)
		char +=1
	return n



if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		O.write (str(solve(I.readline())) +'\n' )