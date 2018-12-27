def sol1(n):
	if n ==0:
		return 0
	if n <=2:
		return 1
	return sol (n-1) + sol (n-2)
def sol2(n):
	ans = 0
	stack =[n]
	while len(stack) != 0:
		cur = stack.pop(0)
		if cur == 0:
			ans += 0
		elif cur <=2:
			ans += 1
		else:
			stack.append(n-1)
			stack.append(n-2)
		print(stack)
	# return ans
if __name__ == '__main__':
	pass