class Pokemon:
    '''
    A generalized pokemon.
    '''

    # General variables could go here

    def __init__(self, p_num, p_name, p_type, p_attack=["Scratch"]):
        '''
        Main initialization code
        '''
        self.number = p_num
        self.name = p_name
        self.p_type = p_type

        # Make sure we have maximum of 4 attacks
        if len(p_attack) > 4:
            raise Exception("Error - Tried generating pokemon with more than 4 attacks")
        if len(p_attack) == 0:
            raise Exception("Error - Tried generating pokemon with 0 attacks")
        self.attacks = p_attack

    def p_print(self):
        print("Pokemon entry %d" % self.number)
        print("\tPokemon name: %s" % self.name)
        print("\tPokemon type: %s" % self.p_type)
        print("\tAttacks: %s" % str(self.attacks))


a = Pokemon(151, "Mew", "Psychic", p_attack=["Psychic", "Transform", "Scratch", "Bite"])
b = Pokemon(150, "Mewtwo", "Psychic", p_attack=["Psychic", "Transform", "Scratch", "Bite"])

a.p_print()
b.p_print()

# pokedex = []
# pokedex.append(Pokemon(1, 'Pikachu', 'Electric', ["Shock", "Tail Whip"]))
# pokedex.append(Pokemon(2, 'Bulbasaur', 'Grass', ["Vine Whip", "Tail Whip"]))
# pokedex.append(Pokemon(3, 'Squirtle', 'Water', ["Watergun", "Tail Whip"]))

# for p in pokedex:
#     p.p_print()
