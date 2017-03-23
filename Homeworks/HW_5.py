import ast

class Game:

    # Goal: make the game grid
    # Read user input & assign blocks, lasers, and points
    # Find alll possible different combinations of boards we can make and run
    # through them all
    def __init__(self, fname):
        # Check that this makes sense
        fptr= open(fname, "r").read()
        lines = fptr.split("\n")
        self.grid = []
        in_grid = False
        self.blocks_avail = []
        self.points = []
        self.lasers = []
        self.a_count, self.b_count, self.c_count = 0,0,0
        self.game_specified = False
        self.availble_spaces = 0

        for line in lines:
            # print line
            # assume that the text file has space after each x and o
            if len(line)==0:
                continue

            if line == "GRID STOP":
                in_grid = False

            if in_grid:
                self.grid.append(line.split(" "))
                for entry in line:
                    if entry =="o":
                        self.availble_spaces +=1

            if line == "GRID START":
                in_grid = True

            # create blocks of the appropriate Type
            # and store them in an array
            # also count the number of blocks to print
            if line[0] in ["A","B", "C"]:
                line = line.split(" ")
                # check how many blocks of one type
                num_blocks = int(line[1])
                for _ in range(num_blocks):
                    self.blocks_avail.append(Block(line[0]))
                    if line[0] == "A":
                        self.a_count+=1
                    if line[0] == "B":
                        self.b_count+=1
                    if line[0] == "C":
                        self.c_count+=1
            # Check if you are specifying points and make points
            # Store the points in an array
            if line[0]=="P":
                temp = line.split(" ")
                x = int(temp[1])
                y = int(temp[2])
                self.points.append(Point(x,y))

            # Do the same with lasers
            if line[0]=="L":
                temp = line.split(" ")
                x_coor = int(temp[1])
                y_coor = int(temp[2])
                dir_x = int(temp[3])
                dir_y = int(temp[4])
                self.lasers.append(Laser(x_coor,y_coor,dir_x,dir_y))
        if len(self.blocks_avail)!= 0 and len(self.points)!=0 and len(self.lasers)!=0 and len(self.grid)!=0:
            self.game_specified=True

    def prnt(self):
        if self.game_specified:
            print "Grid: "
            for row in self.grid:
                print ("\t %s" %row)
            print ("\t Total Available Spaces: %d" %self.availble_spaces)
            print "Available Blocks:"
            print ("\t A %d" %self.a_count)
            print ("\t B %d" %self.b_count)
            print ("\t C %d" %self.c_count)
            print ("Number of laser: %d" %len(self.lasers))
            print ("Number of points: %d" %len(self.points))
        else:
            print "GAME NOT FULLY SPECIFIED."

    def generate_board(self):
        pass

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
        self.dir_x = dir_x
        self.dir_y = dir_y


class Point:
    # points where we want the laser light to intersect
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # may need to put whether it has been hit

a = Game("SETUP.txt")
a.prnt()
