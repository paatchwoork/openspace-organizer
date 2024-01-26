# imports here
import os.path
from os import rename
import pandas as pd
import xlsxwriter as xw

from src.table import Seat
from src.table import Table
from src.openspace import OpenSpace





if __name__ == "__main__":
    
    filename = input("\nPlease specify a file with the list of the people. Only .xlsx files accepted for now ! Thank you ! <3\n")
    if not filename.endswith(".xlsx"): filename+=".xlsx"   #if the file doesn't have an extension, add it

    while not os.path.isfile(filename):     #if the file doesn't exist, continue asking

        print("\n!!! Could not find the specified file !!!          Maybe it's a typo, or the path is wrong ?\n")
        filename = input("Please try again. Thank you ! <3\n")
        if not filename.endswith(".xlsx"): filename+=".xlsx"   #if the file doesn't have an extension, add it

    people = pd.read_excel(filename).iloc[:, 0].tolist()    #read it in a DataFrame and convert back to list


    '''This part asks the user if they want to keep the 6-tables 4-seats layout.
If not, it will ask them the values'''
    while True:

        nb_t = 6
        nb_s = 4

        if len(people) > nb_t*nb_s:

            print("\nIt seems like you have more people than chairs. Some people will not be able to be seated.\nYou might want to increase the number of tables and/or chairs.\n")

        a=input(f"The classroom is initialized with 6 tables that have 4 chairs each, for a total of {nb_t*nb_s} spots.\nDo you want to change that ?\ny/n\n")

        if (a == "y") or (a == "Y"):

            nb_t = int(input("How many tables do you want ?\n"))
            nb_s = int(input("How many seats per table ?\n"))
            break

        elif (a == "n") or (a == "N"):

            break

        else:
            print("Please answer 'y/Y' or 'n/N'\n")


    #Initialize, run and diplay the openspace
    o1=OpenSpace(nb_t, nb_s)
    o1.organize(people)  #take the list of those who couldn't be seated
    o1.display()
    o1.store()
    seated_file = "seated_" + filename
    os.rename("seated.tmp", seated_file)

    print(f"\nYour final openspace organization has been written in {seated_file}\n\nByye <3    ~ Lea")

