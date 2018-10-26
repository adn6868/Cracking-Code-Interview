from sys import stdin as I
from sys import stdout as O
from sys import stderr as E


def solve(m):
	row = []
	col = []
	leng = len(m)
	for i in range(leng):
		for j in range(leng):
			if m[i][j] == '0':
				row.append(i)
				col.append(j)
	for r in row:
		for i in range(leng):
			m[r][i] = '0'
	for c in col:
		for i in range(leng):
			m[i][c] = '0'
		
	return m


if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		n = I.readline()
		m =[]
		for line in range(int(n)):
			m.append(list(I.readline().strip('\n')))
		m = solve(m)
		for line in m:
			O.write (str(line) +'\n')
		O.write('\n')