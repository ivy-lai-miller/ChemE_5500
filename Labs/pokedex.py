import random


class Pokemon:
    '''
    A pokemon object.

    Note, stats includes (give a max of 100 for all):
        Level, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed

    Note, only allow 4 attacks

    Values:

        * num (int)
        * name (str)
        * p_type (list, str)
        * p_attacks (list, str)
        * p_stats (dict, str:int)

    Functions:

        * __init__(num, name, p_type, p_attacks, p_stats)
        * prnt()
    '''

    def __init__(self,num,name,p_type,p_attacks,p_stats):
        self.num = num
        self.name = name
        self.p_type = p_type # list of strings
        self.p_attacks = p_attacks #list with strings for attacks
        self.p_stats = p_stats # dictionary with entries in form string:int

    def prnt(self):
        print ("Pokedex entry: %d" % self.num)
        print ("Pokemon name: %s" % self.name)
        print ("Type: %s" % self.p_type)
        print ("Attacks: %s" %self.p_attacks)
        print ("Stats: ")
        for stat in self.p_stats:
            print ("\t%s\t%d" % (stat, self.p_stats[stat]))



class Pokedex:
    '''
    A pokedex object, to store the discovered pokemon.
    Make a "Not Found" pokemon style for default input.

    Note, have a print out in add.  That is, if we already have the data
    then say so, else say we added new data.

    Values:

        * entries (dict, int:Pokemon)
        * found (int)

    Functions:

        * add(pkmn)
        * prnt(num)
    '''

    def __init__(self):
        self.entries = {}
        self.found = 0


    def add(self,pkmn):
        if pkmn.num in self.entries:
            message = "Pokemon already in Pokedex."
        else:
            self.entries[pkmn.num] = pkmn
            self.entries[pkmn.name] = pkmn
            self.found +=1
            message = "Added %s in Pokedex" % pkmn.name

    def prnt(self, pk_name = None):
        if pk_name == None:
            print "Currently you have %d Pokemon" % self.found
        else:
            if pk_name in self.entries:
                a = self.entries[pk_name]
                a.prnt()
            else:
                "Pokemon not in Pokedex yet."

a_try = Pokemon(
    1, "Bulbasaur", ["Grass", "Poison"], ["Scratch", "Vinewhip"],
    {"Level": 1, "HP": 1, "Attack": 1, "Defense": 1,
     "Sp. Atk": 1, "Sp. Def": 1, "Speed": 1})
# a_try.prnt()
pkdex_try = Pokedex()
pkdex_try.add(a_try)
pkdex_try.prnt("Bulbasaur")

if __name__ == "__main__":
    print("Welcome to Pokemon - CHEME 5500 Edition")

    print('''Use commands like:
    - Go north
    - Go east
    - Go
    - Check Pokedex
    - Get pkmn from pokedex
    - exit
    - quit
    - stop

For example, if I want to print the pokemon data of Pikachu,
I can say:

    get pikachu from pokedex

''')

    # Initialize our variables

    # Make a list of available pokemon
    AVAILABLE_POKEMON = [
        Pokemon(
            1, "Bulbasaur", ["Grass", "Poison"], ["Scratch"],
            {"Level": 1, "HP": 1, "Attack": 1, "Defense": 1,
             "Sp. Atk": 1, "Sp. Def": 1, "Speed": 1}),
        Pokemon(
            2, "Ivysaur", ["Grass", "Poison"], ["Vinewhip"],
            {"Level": 50, "HP": 50, "Attack": 50, "Defense": 50,
             "Sp. Atk": 50, "Sp. Def": 50, "Speed": 50}),
        Pokemon(
            3, "Venusaur", ["Grass", "Poison"], ["Razor Leaf"],
            {"Level": 100, "HP": 100, "Attack": 100, "Defense": 100,
             "Sp. Atk": 100, "Sp. Def": 100, "Speed": 100}),
        Pokemon(
            4, "Charmander", ["Fire"], ["Scratch"],
            {"Level": 1, "HP": 1, "Attack": 1, "Defense": 1,
             "Sp. Atk": 1, "Sp. Def": 1, "Speed": 1}),
        Pokemon(
            5, "Charmeleon", ["Fire"], ["Flamethrower"],
            {"Level": 50, "HP": 50, "Attack": 50, "Defense": 50,
             "Sp. Atk": 50, "Sp. Def": 50, "Speed": 50}),
        Pokemon(
            6, "Charizard", ["Fire", "Flying"], ["Fire Blast"],
            {"Level": 100, "HP": 100, "Attack": 100, "Defense": 100,
             "Sp. Atk": 100, "Sp. Def": 100, "Speed": 100}),
        Pokemon(
            7, "Squirtle", ["Water"], ["Scratch"],
            {"Level": 1, "HP": 1, "Attack": 1, "Defense": 1,
             "Sp. Atk": 1, "Sp. Def": 1, "Speed": 1}),
        Pokemon(
            8, "Wartortle", ["Water"], ["Watergun"],
            {"Level": 50, "HP": 50, "Attack": 50, "Defense": 50,
             "Sp. Atk": 50, "Sp. Def": 50, "Speed": 50}),
        Pokemon(
            9, "Blastoise", ["Water"], ["Hydro Pump"],
            {"Level": 100, "HP": 100, "Attack": 100, "Defense": 100,
             "Sp. Atk": 100, "Sp. Def": 100, "Speed": 100})
    ]

    # Make our pokedex
    pkdex = Pokedex()

    # Have an encounter probability
    PROBABILITY = 0.2

    # Start our game loop
    while 1:
        print("\n")

        # Get user input
        ans = raw_input("What would you like to do? ")
        # Split it into a list of lower case strings
        # Lower case so it's easier to compare against.
        ans = ans.lower().strip().split()

        # If we're moving, then do so here
        if "go" in ans:
            if len(ans) > 1:
                print("... Moving a step to the %s." % ans[-1])
                if ans[-1] == "north" and PROBABILITY < 0.8:
                    PROBABILITY += 0.1
                elif ans[-1] == "south" and PROBABILITY > 0.1:
                    PROBABILITY -= 0.05
            else:
                print("... Taking a random step.")

            # If we moved, check if we encountered a new pokemon
            if random.random() < PROBABILITY:
                print("... Pokemon encountered!")
                pkmn = random.choice(AVAILABLE_POKEMON)
                print("... A wild %s appeared!" % pkmn.name)
                pkdex.add(pkmn)
        # If we want to see how our pokedex is doing, do so
        elif "pokedex" in ans:
            if "check" in ans:
                pkdex.prnt()
            else:
                pkmn_name = ans[ans.index('get') + 1].capitalize()
                pkdex.prnt(pkmn_name)

        # If we want to quit, do so.
        elif "exit" in ans or "quit" in ans or "stop" in ans:
            break

        else:
            print("Unrecognized command.")
            print('''Use commands like:
    - Go north
    - Go east
    - Go
    - Check Pokedex
    - Get pkmn from pokedex
    - exit
    - quit
    - stop

For example, if I want to print the pokemon data of Pikachu,
I can say:

    get pikachu from pokedex

''')

    print("\nThank you for playing!")
