import sys
import math

data = iter(sys.stdin.read().split())

h = int(next(data))
w = int(next(data))
    
if h==1 or w==1:
    print(1)
else:
    print(math.ceil((max(h, w)/2*min(h,w))))
    
    
'''
Since bishop can only move diagonally, atleast half
of the grid's cells can be covered implies the formula. Edge
case is when h==1 or w==1 then we don't have diagonals.
'''
