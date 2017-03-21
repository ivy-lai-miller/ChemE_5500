import time
import random
from PIL import Image

# Our variables
N_blocks = 50
dims = 500

NORTH = (0, 1)
SOUTH = (0, -1)
WEST = (-1, 0)
EAST = (1, 0)
DIRS = [NORTH, SOUTH, EAST, WEST]

# The empty maze - 0 indicates wall, 1 indicates space
maze = [[0 for x in range(N_blocks)] for y in range(N_blocks)]

joe_x = 0
joe_y = 0

# Our list of moves
stack = []
# List of stumbling steps by joe
stack.append((joe_x, joe_y))

# First position starts off as white
maze[0][0] = 1


def save_maze():
    # FUNCTION TO SAVE MAZE TO IMAGE HERE!
    image = Image.new("RGB", (dims,dims))
    pixels = image.load()

    colors = [(0,0,0), (255,255,255)] # black, white
    for xtemp in range(dims):
        for ytemp in range(dims):
            # n/Nblock = x/dims
            # // floors your division
            index = maze[(xtemp*N_blocks)//dims][(ytemp*N_blocks)//dims]
            pixels[xtemp,ytemp] = colors[index]


    image.save("Name.png", "PNG")


def pos_chk(x, y):
    # POSITION CHECK FUNCTION
    return x >= 0 and x <N_blocks and y >= 0 and y <N_blocks


# while len(stack) > 0:
while stack != []:
    # Find all legal moves
    moves = []
    jx, jy = stack[-1]

    for d in DIRS:
        # Check nearby boundaries of new position
        # If total > 1, that means we doubled back
        # Thus, position not allowed.
        x2= jx+d[0] # tentative neighbor location
        y2 = jy+d[1] # tentative neighbor location

        if not pos_chk(x2,y2):
            continue
        # check if you have been here before
        if maze[x2][y2]==1:
            continue

        # check neighbors
        counter = 0
        for d2 in DIRS:
            x3 = x2+d2[0]
            y3 = y2+d2[1]

            if not pos_chk(x3,y3): #if outside the border
                continue
            if maze[x3][y3]==1:
                counter += 1
        if counter != 1:
            continue
        moves.append(d)



    # Randomly grab a move and do it
    # if moves == []:
    if len(moves) == 0:
        # stack.pop()
        del stack[-1]
        # print 'pop'
    else:
        # Take that move
        move = random.choice(moves)
        # MOVE HERE!
        jx += move[0]
        jy += move[1]
        stack.append((jx,jy))
        maze[jx][jy] = 1 # color the block

        save_maze()
        # time.sleep(.4)

save_maze()
