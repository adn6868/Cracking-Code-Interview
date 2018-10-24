from sys import stdin as I
from sys import stdout as O
from sys import stderr as E


def solve(m1):
	n = len(m1)
	m2 =[' '*n]*n
	for i in range(n):
		for j in range(n):
			m2 = m2[j].replace(m2[j][n-i], m1[i][j])
	return m2
	# E.write(n)


if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		n = I.readline()
		m =[]
		for line in range(int(n)):
			m.append(I.readline().strip('\n'))
		O.write (str(solve(m)) +'\n')