from sys import stdin as I
from sys import stdout as O
from sys import stderr as E


def solve(m1):
	n = len(m1)
	m2 =['']*n

	# for i in range(n):
	# 	for j in range(n):
	# 		m2[i] = m1[i][j]+m2[i]
	# E.write(str(m1))
	for i in range(n):
		line = ''
		for j in range(n):
			line += m1[n-1-j][i]
		m2[i] = line
	return m2
	# E.write(n)in

def matrixToString(m):
	for line in m:
		O.write(line+'\n')
	O.write('\n')

if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		n = I.readline()
		m =[]
		for line in range(int(n)):
			m.append(I.readline().strip('\n'))

		matrixToString(solve(m))