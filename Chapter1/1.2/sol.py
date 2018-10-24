from sys import stdin as I
from sys import stdout as O
from sys import stderr as E


def solve(n):
	li = []
	ans= ''
	for char in n:
		ans = char + ans
	return ans



if __name__ == '__main__':
	q = I.readline()
	for i in range(int(q)):
		ans = solve(I.readline())
		O.write(ans+'\n')