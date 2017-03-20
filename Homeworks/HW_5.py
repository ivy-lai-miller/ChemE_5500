import random

class Game:

    # Goal: make the game grid
    # Read user input & assign blocks, lasers, and points
    # Find alll possible different combinations of boards we can make and run
    # through them all
    def __init__(self, fptr):
        pass

class Block:
    # Can be one of the following:
    # Reflecting block: only reflects the lasers
    # Opaque block: absorbs lasers
    # see-through block - both reflects and lets light pass
    def __init__(self):
        self.block_type = random.randint(0,2)


class Laser:
    # store both the starting position and direction of the laser
    def __init__(self):
        pass


class Point:
    # points where we want the laser light to intersect
    def __init__(self):
        pass
