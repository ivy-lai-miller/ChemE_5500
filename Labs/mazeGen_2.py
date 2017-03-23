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
    image = Image.new("RGB", (dims, dims))
    pixels = image.load()

    colours = [(0, 0, 0), (255, 255, 255)]

    for x in range(dims):
        for y in range(dims):
            # math.floor (a / b)
            # a // b
            # int(a / b)
            sx, sy = x * N_blocks, y * N_blocks
            index = maze[sx // dims][sy // dims]
            pixels[x, y] = colours[index]

    image.save("Name.png", "PNG")


def pos_chk(x, y):
    # A function to check if x and y is
    # inside the boundaries

    # if x >= 0 and x < N_blocks and y >= 0 and y < N_blocks:
    #     return True
    # else:
    #     return False

    # return x >= 0 and x < N_blocks and y >= 0 and y < N_blocks

    return x in range(N_blocks) and y in range(N_blocks)


# while len(stack) > 0:
while stack != []:
    # Find all legal moves
    moves = []
    jx, jy = stack[-1]

    for d in DIRS:
        # Check nearby boundaries of new position
        # If total > 1, that means we doubled back
        # Thus, position not allowed.

        x2 = jx + d[0]
        y2 = jy + d[1]

        if not pos_chk(x2, y2):
            continue

        # Have we been here before?
        if maze[x2][y2] == 1:
            continue

        counter = 0
        for d2 in DIRS:
            x3 = x2 + d2[0]
            y3 = y2 + d2[1]

            if not pos_chk(x3, y3):
                continue

            # counter += int(maze[x3][y3] == 1)
            if maze[x3][y3] == 1:
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
        # Move coordinates
        # print jx, jy,
        jx += move[0]
        jy += move[1]
        # print jx, jy
        # Add to stack
        stack.append((jx, jy))
        # Update maze
        maze[jx][jy] = 1
        # 
        # save_maze()
        # time.sleep(1)

save_maze()
