import ast
import itertools
# import random
import copy
import sys

class Game:

    # Goal: make the game grid
    # Read user input & assign blocks, lasers, and points
    # Find alll possible different combinations of boards we can make and run
    # through them all
    # Same setup file as in the assignment
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
        self.available_space = []

        self.block_locations= []
        self.points_location = []

        for line in lines:
            # print line
            # assume that the text file has space after each x and o
            if len(line)==0:
                continue

            if line == "GRID STOP":
                in_grid = False

            if in_grid:
                self.grid.append(line.split(" "))

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
            # Store "in-between" points as 0.5 (ie blocks always on whole numbers)
            # points and lasers may be on half steps
            if line[0]=="P":
                temp = line.split(" ")
                x = float(temp[1])/2
                y = float(temp[2])/2
                self.points.append(Point(x,y))
                self.points_location.append((y,x))

            # Do the same with lasers
            if line[0]=="L":
                temp = line.split(" ")
                x_coor = float(temp[1])/2
                y_coor = float(temp[2])/2
                dir_x = float(temp[3])/2
                dir_y = float(temp[4])/2
                self.lasers.append(Laser(x_coor,y_coor,dir_x,dir_y))

        self.main_board = copy.deepcopy(self.grid)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == "o":
                    self.available_space.append((y,x))
                    self.main_board[y][x] = True
                else:
                    self.main_board[y][x] = False


        if len(self.blocks_avail)!= 0 and len(self.points)!=0 and len(self.lasers)!=0 and len(self.grid)!=0:
            self.game_specified=True


    def prnt(self):
        if self.game_specified:
            print "Grid: "
            for row in self.grid:
                print "\t"+' '.join(row)
                # print ("\t %s" %row)
            print ("\t Total Available Spaces: %d" %len(self.available_space))
            print "Available Blocks:"
            print ("\t A %d" %self.a_count)
            print ("\t B %d" %self.b_count)
            print ("\t C %d" %self.c_count)
            print ("Number of laser: %d" %len(self.lasers))
            print "Laser 1 pointing at: %s %s" %(self.lasers[0].dir_x, self.lasers[0].dir_y)
            print ("Number of points: %d" %len(self.points))
            # print self.available_space
        else:
            print "GAME NOT FULLY SPECIFIED."


    def generate_boards(self):

        def get_partitions(n,k):
            for c in itertools.combinations(range(n+k-1), k-1):
                yield [b-a-1 for a,b in zip((-1,)+c, c + (n+k-1,))]

        partitions = [
            p for p in get_partitions(len(self.blocks_avail),len(self.available_space)) if max(p)==1]

        # print partitions[0]

        # for combination in partitions:
        #     print combination
        boards = []
        for combination in partitions:
            # permu is an array of all possible combinations (A,A,B) or (B,A,A)
            permu = itertools.permutations(self.blocks_avail)

            for case in permu:
                temp_board = copy.deepcopy(self.grid)
                counter_space = 0
                counter_permu = 0
                # print case

                for entry in combination:
                    if entry == 1:
                        y,x = self.available_space[counter_space]
                        temp_board[y][x] = case[counter_permu]
                        counter_permu +=1
                    counter_space +=1

                # print temp_board
                boards.append(temp_board)
        # debugging
        # for board in boards:
        # print boards[0]
        return boards

    # print_board(boards[1])


    def set_board(self,board):
        self.main_board = board
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] not in  ["x","o"]:
                    self.block_locations.append((y,x))
        print "Block locations at: %s" %(self.block_locations)

    def save_board(self,board):
        file_object = open("Board.txt", "w")
        for row in board:
            temp =map(str, row)
            string = ""
            for entry in temp:
                string += entry
            file_object.write(string + "\n")
        file_object.close()

    def print_board(self,board):
        print " "
        for row in board:
            temp = map(str,row)
            print " ".join(temp)



    def run(self):
        print ("Generating all the boards")
        sys.stdout.flush()
        boards = self.generate_boards()
        print ("Done generating boards")
        sys.stdout.flush()

        print "Playing boards..."
        sys.stdout.flush()

        # loop through each board configuration (blocks in place)
        # set the lasers and check if they hit any blocks
        # check if lasers leave board
        # if they hit a block, is the laser ending or reflecting or absorbing?
        # if reflecting, then change the direction of the laser to rotate 90 degrees
        # if absorbing, end the laser
        # if see-through then reflect and also continue light passing
        # store location of each laser hitted spot
        # check if laser hits any points, if so then store the point hit
        # check if every point is hit
        # print len(boards)
        times_entering_loop = 0
        for b_index, board in enumerate(boards):
            self.set_board(board)
            times_entering_loop +=1
            # print board
            points_hit = []

            current_lasers = copy.deepcopy(self.lasers)
            # precounter = 0


            while current_lasers != []:
                # x2, y2 will hold temp position of each lazer "step"
                # for example, if the laser is at 1,3.5 and in direction (1,1) --> really (0.5,0.5)
                # then (x2,y2) will be (1,3.5) then (1.5,4.5) then (2,5) until it is off the board
                laser = current_lasers.pop()
                print current_lasers
                x2= laser.x
                y2 = laser.y


                while y2 < len(self.grid) and x2 < len(self.grid[0]):
                    points_hit.append((x2,y2))
                    # check if you hit a point
                    if (y2,x2) in self.points_location:
                        index = self.points_location.index((y2,x2))
                        self.points[index].hit = True
                        # if not self.points[index].hit:
                        #     self.points[index].hit = True
                        #     precounter +=1
                        #     print "precounter %d" %precounter
                        #     if precounter ==len(self.points):
                        #         break



                        # check if the location will intersect a block
                    # if we are in the middle of a block, do nothing
                    if (x2%1 == 0.5 and y2%1 == 0.5):
                        pass
                    else:
                        l_dir = (laser.dir_x,laser.dir_y)

                        # not going to happen
                        # if l_dir == (0,-0.5):
                        #     xtemp = int(x2)
                        #     ytemp = y2 - 1
                        #     if (xtemp,ytemp) in self.block_locations:

                        if l_dir == (0.5,-0.5):
                            print "ldir is %s %s" %l_dir
                            if x2%1 == 0.5:
                                xtemp = int(x2 - 0.5)
                                ytemp = int(y2)
                            # Case 2: x-cor is int (hit from side)
                            else:
                                xtemp = int(x2)
                                ytemp = int(y2 - 0.5)
                            if (ytemp,xtemp) in self.block_locations:
                                tempblock = self.main_board[ytemp][xtemp]
                                if tempblock.absorbs:
                                    break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue
                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = 0.5
                                        l_ydir = 0.5
                                    else:
                                        l_xdir = -0.5
                                        l_ydir = -0.5
                                    current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    if not tempblock.light_pass:
                                        break

                        if l_dir == (0.5,0.5):
                            print "ldir is %s %s" %l_dir
                            # Case 1: x-cor is not int (hit from top)
                            if x2%1 == 0.5:
                                xtemp = int(x2 - 0.5)
                                ytemp = int(y2)
                            # Case 2: x-cor is int (hit from side)
                            else:
                                xtemp = int(x2)
                                ytemp = int(y2 - 0.5)
                            # print (xtemp,ytemp)
                            if (ytemp,xtemp) in self.block_locations:
                                # print "Collision with block"
                                tempblock = self.main_board[ytemp][xtemp]
                                if tempblock.absorbs:
                                    break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue
                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = 0.5
                                        l_ydir = -0.5
                                    else:
                                        l_xdir = -0.5
                                        l_ydir = 0.5
                                    print "Laser(%s,%s,%s,%s)" % (x2,y2,l_xdir,l_ydir)
                                    current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    if not tempblock.light_pass:
                                        break

                        if l_dir == (-0.5,0.5):
                            print "ldir is %s %s" %l_dir
                            # Case 1: x-cor is not int (hit from top)
                            if x2%1 == 0.5:
                                xtemp = int(x2 - 0.5)
                                ytemp = int(y2)
                            # Case 2: x-cor is int (hit from right side)
                            else:
                                xtemp = int(x2-1)
                                ytemp = int(y2-0.5)
                            if (ytemp,xtemp) in self.block_locations:
                                tempblock = self.main_board[ytemp][xtemp]
                                if tempblock.absorbs:
                                    break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue
                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = -0.5
                                        l_ydir = -0.5
                                    else:
                                        l_xdir = 0.5
                                        l_ydir = 0.5
                                    current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    if not tempblock.light_pass:
                                        break


                        if l_dir == (-0.5,-0.5):
                            print "ldir is %s %s" %l_dir
                            # Case 1: x-cor is not int (hit from bottom)
                            if x2%1 == 0.5:
                                xtemp = int(x2 - 0.5)
                                ytemp = int(y2-1)
                            # Case 2: x-cor is int (hit from right side)
                            else:
                                xtemp = int(x2-0.5)
                                ytemp = int(y2-1)
                            if (ytemp,xtemp) in self.block_locations:
                                tempblock = self.main_board[ytemp][xtemp]
                                if tempblock.absorbs:
                                    break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue
                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = -0.5
                                        l_ydir = 0.5
                                    else:
                                        l_xdir = 0.5
                                        l_ydir = -0.5

                                    current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    if not tempblock.light_pass:
                                        break
                    # Update to next step block
                    x2 = x2+laser.dir_x
                    y2 = y2+laser.dir_y
            print board
            print "Points hit %s" %points_hit
            hit_counter = 0
            for entry in self.points:
                if entry.hit:
                    hit_counter+=1
            if hit_counter == len(self.points):
                self.save_board(board)
                print "Winning board found"
                break
        print "Done running"
        print times_entering_loop









class Block:
    # Can be one of the following:
    # Reflecting block: only reflects the lasers
    # Opaque block: absorbs lasers
    # see-through block - both reflects and lets light pass
    # block_values=["A","B","C"]
    def __init__(self,value):
        value_up = value.upper()
        self.reflects = (value_up == "A" or value_up == "C")
        self.absorbs = (value_up == "B")
        self.light_pass = (value_up=="C")
        self.block_type = value_up

    def __repr__(self):
        return str(self.block_type)

    def __str__(self):
        return str(self.block_type)

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
        self.hit = False
        # may need to put whether it has been hit

a = Game("SETUP_debug.txt")
a.prnt()
a.run()
# boards = a.generate_boards()
# a.print_board(boards[1])
# print type(boards[1][3][1])
# a.print_board(boards[0])
# a.print_board(boards[2])
# a.print_board(boards[3])
# a.save_board(boards[1])
