#!/bin/python
def nextMove(n,r,c,grid):
    pr = 0
    pc = 0
    for i,j in zip(grid,range(len(grid))) :
        for k,l in zip(i,range(len(grid))) :
            if k == 'p' :
                pc = l
                pr = j
    if(r != pr) :
    	if(r < pr) :
    		return "DOWN"
    	else :
    		return "UP"
    else if(c != pc) :
    	if(c < pc) :
    		return "RIGHT"
    	else :
    		return "LEFT"
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)