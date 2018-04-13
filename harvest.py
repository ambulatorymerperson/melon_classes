############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
    # code = None
    # first_harvest = None
    # color = None
    # pairings = []
    # is_seedless = None
    # is_bestseller = None

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller=None):
        """Initialize a melon."""
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        return self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        return self.code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []


    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    cas = MelonType('cas', 'Casaba', 2003, 'orange', False)
    cas.add_pairing('strawberries', 'mint')
    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False)
    cren.add_pairing('proscuitto')
    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')

    all_melon_types.append(musk)
    all_melon_types.append(cas)
    all_melon_types.append(cren)
    all_melon_types.append(yw)

    return all_melon_types

# def simple(melon_types):
#     print "hi " + str(melon_types)
# simple(make_melon_types())

# print yw.dict 
# print all_melon_types[0]
# print MelonType.__dict__

def print_pairing_info(all_melon_types):
    """Prints information about each melon type's pairings."""
    for item in all_melon_types:
        item.pairings = item.pairings[0]
        if len(item.pairings) >= 2:
            print "{} pairs with\n- {} and {}".format(item.name, item.pairings[0], item.pairings[1])
        else:
            print "{} pairs with \n-{}".format(item.name, item.pairings[0])


print_pairing_info(make_melon_types())


def make_melon_type_lookup(all_melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for item in all_melon_types:
        melon_dict[item.code] = item.name

    print melon_dict    

############
# Part 2   #
############
make_melon_type_lookup(make_melon_types())
class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 

