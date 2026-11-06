# len gives the length of a list

planets = ['Mercury', 'Venues', 'Saturn']
len(planets)


def fashionably_late(arrivals, name):
    """
    Return True if 'name' arrived after at least half of the other guests had arrived, but was
    not the last guest to arrive
    """

    if name not in arrivals:
        return False

    order = arrivals.index(name)
    # the .index method returns the position of the first occurence of a specified value within a sequence like a list
    # create the order variable and in it store the positions of the guests, 'name' within the arrivals list
    # order is literally the person's position in the list
    n=len(arrivals)
    # assign the length of the list to variable n
    # n is the total number of people
    return 2 * order >= n and order != n -1
    # this line literally says, return TRUE ONLY IF the conditions are true
    # the conditions are that the person should arrive after at least half the gust and they are not the last person

