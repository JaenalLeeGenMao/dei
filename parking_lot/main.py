from __future__ import print_function
from parking_lot import *

import sys

def read_file(file_name):

    collection = []

    # Looping through the files and return as list format
    with open(file_name, 'r') as data:

        for line in data:

            collection.append(line.replace('\n', '').split(' '))

    return collection

def main():

    data = read_file(sys.argv[1])
    parking_slot = []
    parking_lot = Parking_lot()

    for current in data:

        info = current[0]

        if (info == "create_parking_lot"):

            n = current[1]
            parking_slot = parking_lot.create_parking_slot(n)
            print("Created a parking lot with " + str(len(parking_slot)) + " slots")

        elif (info == "park"):

            parking_info = parking_lot.assign_parking(parking_slot, current)

            if (parking_info == -1):
                print("Sorry, parking lot is full")
            else:
                print("Allocated slot number: ", parking_info + 1)

        elif (info == "leave"):

            index = current[1]
            parking_lot.remove_parking(parking_slot, index)

        elif (info == "status"):
            parking_lot.status(parking_slot)

        elif (info == "registration_numbers_for_cars_with_colour"):
            colour = current[1]
            parking_lot.registration_numbers_for_cars_with_colour(parking_slot, colour)

        elif (info == "slot_numbers_for_cars_with_colour"):
            colour = current[1]
            parking_lot.slot_numbers_for_cars_with_colour(parking_slot, colour)

        elif (info == "slot_number_for_registration_number"):
            registry_no = current[1]
            parking_lot.slot_number_for_registration_number(parking_slot, registry_no)

    # close the parking state
    parking_lot.close()

main()
