class Seat:
    """
    Defines a seat with its free (or not) status and who's occupying it.

    ATTRIBUTES
    occupant is the name of the person who occupuies that seat
    free is a boolean that is True if the seat is free

    METHODS
    set_occupant allows to put a new person at the table and sets its 
        free value to False.
    remove_occcupant allows to remove an occupant from a table and sets
        its free vale to True.

    """

    def __init__(self, occupant: str = "", free: bool = True):
        self.free = free
        self.occupant = occupant

    def __str__(self):
        return f"This is a Seat() object, free = {self.free} and occupant = {self.occupant}"

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        if not self.free:
            self.occupant = ""
            self.free = True


class Table:
    """Defines a table with its seats (which are Seat objects as 
        defined above) its capacity (i.e. the number of seats).

    ATTRIBUTES
    capacity is an integer and needs to be set upon instanciating
    seats is a list of capacity-number of Seat objects

    METHODS
    has_free_spot() return True if there is a free spot, and False 
        if there is none
    capacity_left() will return the number of free seats at the table
    assign_seat(name) takes the name of the person, and puts it on 
        the first empty seat of the table
    """

    def __init__(self, capacity: int, seats: list = []):
        self.capacity = capacity  # initializing capacity
        self.seats = []

        for s in range(capacity):
            self.seats.append(Seat())

    def __str__(self):
        return f"This is a Table() object, capacity = {self.capacity}"

    # Is there a free spot at this table ?
    def has_free_spot(self):
        return any(
            [s.free for s in self.seats]
        )  # returns True is the table has a free seat, otherwise returns False

    # How many empty seats left ?
    def capacity_left(self):
        nbfree = 0
        if self.has_free_spot():
            for s in self.seats:
                if s.free:
                    nbfree += 1
        return nbfree

    # Hey guys do you mind if I sit with you ?
    def assign_seat(self, name):
        for s in self.seats:
            if s.free:  # if the seat is empty...
                s.set_occupant(name)  # fill it with an occupant
                break  # and stop looking for an empty seat
