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
        * readPokemon(fptr)
        * writePokemon(fptr)
        * prnt()
    '''
    def __init__(self, num, name, p_type, p_attacks, p_stats):
        self.num = num
        self.name = name
        self.p_type = p_type
        self.p_attacks = p_attacks
        self.p_stats = p_stats

    def readPokemon(self, fptr):
        raise Exception("Unable to read pokemon yet.")

    def writePokemon(self, fptr):
        raise Exception("Unable to write pokemon yet.")

    def prnt(self):
        print("Pokemon %d - %s" % (self.num, self.name))
        print("\tThis pokemon is of type %s" % " and ".join(self.p_type))
        print("\tAttacks:")
        for atk in self.p_attacks:
            print("\t\t%s" % atk)
        print("\tStats:")

        keys = ["Level", "HP", "Attack", "Defense",
                "Sp. Atk", "Sp. Def", "Speed"]

        for k in keys:
            print("\t\t%s = %d" % (k, self.p_stats[k]))


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

    def add(self, pkmn):
        if pkmn.num in self.entries:
            print("Data for %s aleady found." % pkmn.name)
        else:
            print("Adding data for %s." % pkmn.name)

            # NOTE! We store it twice, once by name and once by number.
            # This makes it easier for the user to get the data back.
            self.entries[pkmn.num] = pkmn
            self.entries[pkmn.name] = pkmn
            self.found += 1

    def prnt(self, pkmn_name=None):
        if pkmn_name is None:
            print("Currently you have found %d pokemon!" % self.found)
        else:
            if pkmn_name in self.entries:
                self.entries[pkmn_name].prnt()
            else:
                print("Unfortunately you have not found a pokemon named %s."
                      % pkmn_name)


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