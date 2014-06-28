def nextMove(grid) :
	if grid[0][1] != '#':
		return "UP"
	elif grid[1][0] != '#':
		return "LEFT"
	elif grid[1][2] != '#':
		return "RIGHT"
	elif grid[2][1] != '#':
		return "DOWN"


prevDirection = open("prevDirection.txt",'w')
n = input()
grid = []
for i in xrange(0, 3):
    grid.append(raw_input())

print nextMove(grid)