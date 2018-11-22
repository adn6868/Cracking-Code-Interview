from Tree import *
def main():
	a = Tree(3)
	b = Tree(4)
	c = Tree(5)
	d = Tree(6)
	e = Tree(7)
	f = Tree(8)
	g = Tree(9)


	a.addChild(b)
	a.addChild(c)
	b.addChild(d)
	b.addChild(e)
	b.addChild(f)
	c.addChild(g)

	print(a.toString()) 
if __name__ == '__main__':
	main()