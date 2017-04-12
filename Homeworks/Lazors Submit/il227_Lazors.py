import ast
import itertools
import copy
import sys

class Game:

    # Goal: make the game grid
    # Read user input & assign blocks, lasers, and points
    # Find alll possible different combinations of boards we can make and run
    # through them all
    # Same setup file as in the assignment
    def __init__(self, fname):
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
        self.points_location = []
        self.original_block_locations = []

        for line in lines:
            # assume that the text file has space after each x and o
            if len(line)==0:
                continue

            if line == "GRID STOP":
                in_grid = False

            if in_grid:
                self.grid.append(line.split())

            if line == "GRID START":
                in_grid = True

            # create blocks of the appropriate Type
            # and store them in an array
            # also count the number of blocks to print
            if not in_grid and line[0] in ["A","B", "C"]:
                line = line.split()
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
                temp = line.split()
                x = float(temp[1])/2
                y = float(temp[2])/2
                self.points.append(Point(x,y))
                self.points_location.append((y,x))

            # Do the same with lasers
            if line[0]=="L":
                temp = line.split()
                x_coor = float(temp[1])/2
                y_coor = float(temp[2])/2
                dir_x = float(temp[3])/2
                dir_y = float(temp[4])/2
                self.lasers.append(Laser(x_coor,y_coor,dir_x,dir_y))

        self.main_board = copy.deepcopy(self.grid)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                # For debugging:
                # print self.grid[y][x]
                if self.grid[y][x] == "o":
                    self.available_space.append((y,x))
                    # self.main_board[y][x] = True
                if self.grid[y][x] in ["A", "B", "C"]:
                    # self.main_board[y][x] = Block(self.grid[y][x])
                    self.grid[y][x] = Block(self.grid[y][x])
                    self.original_block_locations.append((y,x))
                # else:
                #     self.main_board[y][x] = False


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
            # For debugging
            # print "Laser 1 pointing at: %s %s" %(self.lasers[0].dir_x, self.lasers[0].dir_y)
            print ("Number of points: %d" %len(self.points))
            # print self.available_space
        else:
            print "GAME NOT FULLY SPECIFIED."
            # print "Grid: "
            # for row in self.grid:
            #     print "\t"+' '.join(row)
            #     # print ("\t %s" %row)
            # print ("\t Total Available Spaces: %d" %len(self.available_space))
            # print "Available Blocks:"
            # print ("\t A %d" %self.a_count)
            # print ("\t B %d" %self.b_count)
            # print ("\t C %d" %self.c_count)
            # print ("Number of laser: %d" %len(self.lasers))
            # # For debugging
            # # print "Laser 1 pointing at: %s %s" %(self.lasers[0].dir_x, self.lasers[0].dir_y)
            # print ("Number of points: %d" %len(self.points))


    def generate_boards(self):

        def get_partitions(n,k):
            for c in itertools.combinations(range(n+k-1), k-1):
                yield [b-a-1 for a,b in zip((-1,)+c, c + (n+k-1,))]

        # For debugging:
        # print len(self.blocks_avail)
        # print len(self.available_space)
        partitions = [
            p for p in get_partitions(len(self.blocks_avail),len(self.available_space)) if max(p)==1]

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
        return boards


    def set_board(self,board):
        self.main_board = board
        self.block_locations = copy.deepcopy(self.original_block_locations)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] not in  ["x","o"]:
                    self.block_locations.append((y,x))
        # For debugging
        # print "Block locations at: %s" %(self.block_locations)
        # print board

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

        # write a function that helps us check if a coordinate is still in the board
        def poschk(x,y):
            return y >= 0 and y <= len(self.main_board) and x >=0 and x <= len(self.main_board[0])

        # loop through each board configuration (blocks in place)
        # set the lasers and check if they hit any blocks or points
        # if a point is hit, then we will set the status of that point to already hit
        # at the end, if all points are hit, we have the winning board

        # For debugging (check how many times you enter the loop)
        times_entering_loop = 0
        for b_index, board in enumerate(boards):
            self.set_board(board)
            # for debugging
            times_entering_loop +=1
            # path_hit will store path traveled by the laser (reset each board)
            path_hit = []

            # create a copy of lasers (so you won't change the actual lasers available each run)
            current_lasers = copy.deepcopy(self.lasers)
            # precounter = 0


            while current_lasers != []:

                # For debugging
                # print current_lasers

                # Take the last entry in the array and do a run-through with that laser
                laser = current_lasers.pop()

                # x2, y2 will hold temp position of each lazer "step"
                # for example, if the laser is at 1,3.5 and in direction (1,1) --> really (0.5,0.5)
                # then (x2,y2) will be (1,3.5) then (1.5,4.5) then (2,5) until it is off the board
                x2= laser.x
                y2 = laser.y
                # For debugging
                # print x2,y2

                while poschk(x2,y2):
                    # Do a check to see if we are in a infinite loop of lasers (Example: MAD 2)
                    # This means we have been at the point before, coming from the same direction
                    # if so, we should move on to the next laser
                    if ((x2,y2), (laser.dir_x,laser.dir_y)) in path_hit:
                        break


                    # if not in a loop, we should step to the new spot and record
                    # that we have been here from our current direction
                    path_hit.append(((x2,y2), (laser.dir_x,laser.dir_y)))

                    # First check if you hit a point
                    if (y2,x2) in self.points_location:
                        index = self.points_location.index((y2,x2))
                        self.points[index].hit = True



                    # Second, check if the location will intersect a block
                    # if we are in the middle of a block, do nothing
                    if (x2%1 == 0.5 and y2%1 == 0.5):
                        pass

                    # Here check each direction we could be coming from
                    # since it has a different result (where to bounce or continue)
                    # we assume that lasers are hitting from an angle (never horizontal or vertical)
                    else:
                        l_dir = (laser.dir_x,laser.dir_y)


                    # for each direction, a laser can be hitting a block from the top/bottom or from the sides
                    # if the x-coordinate is an int we know that it is hitting from top/bottom
                    # otherwise, laser must be hitting one of the sides

                    # also note that blocks are stored on the top left of a grid

                        # Checking direction 1 (0.5,-0.5)
                        if l_dir == (0.5,-0.5):
                            # For debugging:
                            # print "ldir is %s %s" %l_dir

                            # Case 1: x-cor isn't int (hit from bottom)
                            if x2%1 == 0.5:
                                xtemp = int(x2 - 0.5)
                                ytemp = int(y2-1)
                            # Case 2: x-cor is int (hit from side)
                            else:
                                xtemp = int(x2)
                                ytemp = int(y2 - 0.5)
                            if (ytemp,xtemp) in self.block_locations:
                                tempblock = self.main_board[ytemp][xtemp]
                                if tempblock.absorbs:
                                    break

                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = 0.5
                                        l_ydir = 0.5
                                        if not (int(y2),int(x2-0.5)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    else:
                                        l_xdir = -0.5
                                        l_ydir = -0.5
                                        if not (int(y2-0.5),int(x2-1)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    if not tempblock.light_pass:
                                        break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue

                        # Checking direction 2 (0.5,0.5)
                        if l_dir == (0.5,0.5):
                            # print "ldir is %s %s" %l_dir
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

                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = 0.5
                                        l_ydir = -0.5
                                        if not (int(y2-1),int(x2-0.5)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    else:
                                        l_xdir = -0.5
                                        l_ydir = 0.5
                                        if not (int(y2-0.5),int(x2-1)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    if not tempblock.light_pass:
                                        break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue

                        # Checking direction 3 (-0.5,0.5)
                        if l_dir == (-0.5,0.5):
                            # print "ldir is %s %s" %l_dir
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

                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = -0.5
                                        l_ydir = -0.5
                                        if not (int(y2-1),int(x2-0.5)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    else:
                                        l_xdir = 0.5
                                        l_ydir = 0.5
                                        if not (int(y2-0.5),int(x2)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    if not tempblock.light_pass:
                                        break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue

                        # Checking direction 4 (-0.5,-0.5)
                        if l_dir == (-0.5,-0.5):
                            # print "ldir is %s %s" %l_dir
                            # Case 1: x-cor is not int (hit from bottom)
                            if x2%1 == 0.5:
                                xtemp = int(x2 - 0.5)
                                ytemp = int(y2-1)
                            # Case 2: x-cor is int (hit from right side)
                            else:
                                xtemp = int(x2-1)
                                ytemp = int(y2-0.5)
                            if (ytemp,xtemp) in self.block_locations:
                                tempblock = self.main_board[ytemp][xtemp]
                                if tempblock.absorbs:
                                    break

                                if tempblock.reflects:
                                    # checks cases again to assign new direction
                                    if x2%1 == 0.5:
                                        l_xdir = -0.5
                                        l_ydir = 0.5
                                        if not (int(y2),int(x2-0.5)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))
                                    else:
                                        l_xdir = 0.5
                                        l_ydir = -0.5
                                        if not (int(y2-0.5),int(x2)) in self.block_locations:
                                            current_lasers.append(Laser(x2+l_xdir,y2+l_ydir,l_xdir,l_ydir))

                                    if not tempblock.light_pass:
                                        break
                                if tempblock.light_pass:
                                    x2 = x2+laser.dir_x
                                    y2 = y2+laser.dir_y
                                    continue

                    # Update to next location we will check
                    x2 = x2+laser.dir_x
                    y2 = y2+laser.dir_y
            # For debugging
            # print board
            # print "Path hit %s" %path_hit

            # Reset the hit counter (for debugging)
            hit_counter = 0

            # Check if every point is hit (if so, we win)
            # Also reset the value of hit to False
            for entry in self.points:
                if entry.hit:
                    hit_counter+=1
                entry.hit = False

            # If we found a winning board, we quit (Check w/ Henry to see if this is allowed)
            if hit_counter == len(self.points):
                self.save_board(board)
                print "Winning board found"
                # print self.points
                # For debugging:
                # print hit_counter
                break
        print "Done running"
        # For debugging
        # print times_entering_loop



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
    # x,y are the x and y coordinates of the laser origin (where it starts)
    # dir_x, dir_y tell us the direction the laser is pointing at
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
        # Each point will carry whether or not it has been hit
        # This needs to be reset each board
        # The reason we don't carry it in an array is because its ok if its hit
        # more than one time as long as it hit (so a counter won't work but a list or just a property will)
        self.hit = False


a = Game("mad_1.input")
# a.prnt()
a.run()
