import ast

class Game:

    # Goal: make the game grid
    # Read user input & assign blocks, lasers, and points
    # Find alll possible different combinations of boards we can make and run
    # through them all
    def __init__(self, fptr):
        # Check that this makes sense
        self.read()

    def read(self):
        fptr = open("SETUP.txt", "r").read()
        lines = fptr.split("\n)
        grid = []
        in_grid = False
        a_count, b_count, c_count
        for line in lines:
            if in_grid:
                temp = line.strip()
                grid.append(temp)

            if line == "GRID START":
                in_grid = True


            if line == "GRID STOP":
                in_grid = False

            if line[0]=="A":
                temp = line.strip()
                a_count = temp[1]
            if line[0]=="B":
                temp = line.strip()
                b_count = temp[1]
            if line[0]=="C":
                temp = line.strip()
                c_count = temp[1]








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
    def __init__(self,x=0,y=0,direction):
        self.x = x
        self.y = y
        self.direction = direction


class Point:
    # points where we want the laser light to intersect
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # may need to put whether it has been hit
