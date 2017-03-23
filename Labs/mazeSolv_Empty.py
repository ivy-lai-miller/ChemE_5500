import time
import random
from PIL import Image


def load_maze(fname, N_blocks=50):
    # Load maze
    img = Image.open(fname)
    dim_x, dim_y = img.size

    maze = [[0 for x in range(N_blocks)] for y in range(N_blocks)]

    for i, x in enumerate(range(0, dim_x, dim_x // N_blocks)):
        for j, y in enumerate(range(0, dim_y, dim_y // N_blocks)):
            px = x
            py = y
            maze[i][j] = int(img.getpixel((px, py)) == (255, 255, 255))
            # checks if white, and if so, returns boolean "1" which is also for white
    return maze, dim_x


N_blocks = 50
maze, dims = load_maze("Name.png", N_blocks=N_blocks)

maze_start = (0, 0)
maze_end = (49, 49)
NORTH = (0, 1)
SOUTH = (0, -1)
WEST = (-1, 0)
EAST = (1, 0)
DIRS = [NORTH, SOUTH, EAST, WEST]
stack = [maze_start]

maze[maze_start[0]][maze_start[1]] = 4
maze[maze_end[0]][maze_end[1]] = 4

def save_maze():
    # FUNCTION TO SAVE MAZE TO IMAGE HERE!
    image = Image.new("RGB", (dims, dims))
    pixels = image.load()

    colours = [(0, 0, 0), (255, 255, 255), (255,0,0), (0,255,0), (0,0,255)]

    for x in range(dims):
        for y in range(dims):
            # math.floor (a / b)
            # a // b
            # int(a / b)
            sx, sy = x * N_blocks, y * N_blocks
            index = maze[sx // dims][sy // dims]
            pixels[x, y] = colours[index]

    image.save("Solved.png", "PNG")

def pos_chk(x, y):
    # POSITION CHECK FUNCTION
    return x in range(N_blocks) and y in range(N_blocks)


while stack != []:
    # Find all legal moves
    moves = []
    jx, jy = stack[-1]

    for d in DIRS:
        # Check nearby boundaries of new position
        x2= jx+d[0] # tentative neighbor location
        y2 = jy+d[1] # tentative neighbor location

        if not pos_chk(x2,y2):
            continue
        # Am i allowed here?
        if maze[x2][y2]==1 or maze[x2][y2]==4:
            moves.append(d)
        # Randomly grab a move and do it
        # if moves == []:
    if len(moves) == 0:
        # if there are no moves, then assign that block red color
        maze[jx][jy]=2
        del stack[-1]
        # print stack

    else:
        # Take that move
        move = random.choice(moves)
        # MOVE HERE!
        # print move
        jx += move[0]
        jy += move[1]

        if jx == maze_end[0] and jy == maze_end[1]:
            maze[jx][jy] = 4
            maze[maze_start[0]][maze_start[1]] = 4
            break

        stack.append((jx,jy))
        # print jx,jy
        maze[jx][jy] = 3
        # color the block green
        # save_maze()

save_maze()
