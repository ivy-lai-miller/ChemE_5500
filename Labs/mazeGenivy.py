from PIL import Image # need to write an image
import random # random to make maze

block_size =  10 # each block will be 10x10 pixels large
dims = 256

''' Algorithm

1. Where can I go? Cannot loop back to make cavern. --> Directions
2. Boundaries
3. Go back if you cannot move any more
'''

# maze will be a 2D list
# you can do so by list comprehension or using for loop

# example = [x for x in range(100)] # gives a list from 0 to 99
# example = [1 for x in range(100)] # gives a list of one hundred ones

# make maze with list comprehension
# 0 indicats wall, 1 indicates space
maze = [[0 for x in range(dims)] for y in range(dims)]

# Define Directions as tuples
NORTH = (0,1)
SOUTH = (0, -1)
WEST = (-1,0)
EAST = (1,0)

DIRS = [NORTH,SOUTH,WEST,EAST]

# make stack to carry the location of the path traveled (for algorithm)
# Our list of moves
stack = []

joe_x = 0
joe_y = 0
joe_dir = NORTH # direction that joe came from


# List of stumbling stacks by joe
stack.append((joe_x, joe_y, joe_dir))

# First position starts off as white
maze[0][0] = 1

while len(stack) > 0: # while stack != []:
    # Find all legal moves
    moves = []
    jx,jy,jd = stack[-1]

    for d in DIRS:
        if d == jd:
            continue
        # Check nearby boundaries (is he leaving maze or is he closing)
        # if total filled neighbors > 1, that means we doubled back (position not allowed)

        # ELSE save new position



    # Randomly grab a move and do it
    if len(moves) == 0:
        stack.pop()
    else:
        # Take that move


    # maze[i][j] = 1

    # UNLESS no legal moves. If so, delete last move

# Save maze















# end
