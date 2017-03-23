import ast

class Game:

    # Goal: make the game grid
    # Read user input & assign blocks, lasers, and points
    # Find alll possible different combinations of boards we can make and run
    # through them all
    def __init__(self, fptr):
        # Check that this makes sense
        ptr = open("SETUP.txt", "r").read()
        lines = fptr.split("\n")
        grid = []
        in_grid = False
        a_count, b_count, c_count
        points = []
        lasers = []
        for line in lines:
            # assume that the text file has space after each x and o
            if in_grid:
                grid.append(line.strip(" "))

            if line == "GRID START":
                in_grid = True


            if line == "GRID STOP":
                in_grid = False

            # store values for block types and number
            if line[0]=="A":
                a_count = int(line[2:])
            if line[0]=="B":
                b_count = int(line[2:])
            if line[0]=="C":
                c_count = int(line[2:])

            if line[0]=="P":
                temp = line.split(" ")
                x = int(temp[1])
                y = int(temp[2])
                points.append(Point(x,y))

            if line[0]=="L":
                temp = line.split(" ")
                x_coor = int(temp[1])
                y_coor = int(temp[2])
                dir_x = int(temp[3])
                dir_y = int(temp[4])
                lasers.append(Laser(x_coor,y_coor,dir_x,dir_y))

    NORTH = (0, 1)
    SOUTH = (0, -1)
    WEST = (-1, 0)
    EAST = (1, 0)
    DIRS = [NORTH, SOUTH, EAST, WEST]



class Block:
    # Can be one of the following:
    # Reflecting block: only reflects the lasers
    # Opaque block: absorbs lasers
    # see-through block - both reflects and lets light pass
    # block_values=["A","B","C"]
    def __init__(self,value):
        value_up = value.upper()
        self.reflects = (value_up == "A" or value_up == "C")
        self.absorbs = (value_up == "B" or value_up == "C")
        self.block_type = value_up


class Laser:
    # store both the starting position and direction of the laser
    def __init__(self,x,y,dir_x, dir_y):
        self.x = x
        self.y = y
        self.direction = (dir_x,dir_y)


class Point:
    # points where we want the laser light to intersect
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # may need to put whether it has been hit
