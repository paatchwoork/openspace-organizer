from random import randint
from random import shuffle
import xlsxwriter as xw

from src.table import Table


class OpenSpace:
    """
    Defines an openspace, with tales, which contain seats.

    ATTRIBUTES
    number_of_tables is the number of tables in the openspace
    number_of_seats is the number of seats per table
    tables is a list of Table() objects

    METHODS
    display prints the status of the table in the terminal, in a nice 
        and neat way
    organize takes a list of people and randomly places them at a 
        table
    store puts the list of people and their placement in a seated.tmp 
        file that will be read by the main.py module
    """

    def __init__(
        self, number_of_tables: int, number_of_seats: int, tables: list = []
    ):
        self.number_of_tables = (
            number_of_tables  # initializing number_of_tables
        )
        self.number_of_seats = number_of_seats  # initializing number_of_seats

        self.not_seated = []  # only used if there are too many people

        self.tables = tables  # initializing tables
        for t in range(number_of_tables):
            self.tables.append(Table(number_of_seats))

    def __str__(self):
        return f"This is an OpenSpace object that has {self.number_of_tables} tables and {self.number_of_seats} seats. {len(self.not_seated)} could't be seated."

    # Prints the disposition of people in the classroom
    def display(self):
        for t, table in enumerate(self.tables):
            print(f"\nTable {t+1}")
            for s, seat in enumerate(table.seats):
                print(seat.occupant)
            seat_number = 0

    # Randomly places people at the seats
    def organize(self, names: list):
        nb_seated = 0

        for person in names:  # take the each person
            # This will stop placing people at tables once everyone has been seated
            if nb_seated == self.number_of_tables * self.number_of_seats:
                self.not_seated = names[nb_seated + 1 :]
                break

            # stores the names of those who couldn't be seated
            if nb_seated == (self.number_of_tables * self.number_of_seats):
                self.not_seated = names[
                    nb_seated + 1 :
                ]  # puts al trhe unseated people in a list that will be read by the store() method

            while (
                True
            ):  # infinite loop that will break if the person finds a table
                assigned_table = randint(
                    0, len(self.tables) - 1
                )  # choose a random table
                assigned_seat = randint(
                    0, self.tables[assigned_table].capacity
                )  # choose a random seat on that table

                if self.tables[
                    assigned_table
                ].has_free_spot():  # if the table has a free spot
                    self.tables[assigned_table].assign_seat(
                        person
                    )  # put that person there
                    nb_seated += 1  # one more person has been seated
                    break

    def store(self):
        # Open an xlsx file
        book = xw.Workbook("seated.tmp")
        sheet = book.add_worksheet()

        # Input the seated people
        for t, table in enumerate(self.tables):
            sheet.write(0, t, f"Table {t+1}")
            end_table = t
            for s, seat in enumerate(table.seats):
                sheet.write(s + 1, t, seat.occupant)

        # Input the unseated people
        sheet.write(0, end_table + 1, "Not seated")
        for ns, noseat in enumerate(self.not_seated):
            sheet.write(ns + 1, end_table + 1, noseat)

        book.close()
