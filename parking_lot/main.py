from __future__ import print_function

def create_parking_slot(n):

    n = int(n)
    # Verify if input is at least 2 inputs
    if (n < 2):
        return "Please input a list greater or equal 2"

    # create parking slot list and return the list
    parking_slot = [None] * n
    return parking_slot

def read_file(file_name):

    collection = []

    # Looping through the files and return as list format
    with open(file_name, 'r') as data:

        for line in data:

            collection.append(line.replace('\n', '').split(' '))

    return collection

def assign_parking(parking_slot, current_car):

    # looping through the parking slot to find a slot for current car
    for each_slot in range(len(parking_slot)):
        # if slot is empty, successfully allocated to a slot then return index of the allocated slot
        if (parking_slot[each_slot] == None):

            parking_slot[each_slot] = current_car
            return each_slot

    # if no slots are available return -1
    return -1

def remove_parking(parking_slot, index):

    index = int(index) - 1
    # Verify if input is at least 2 inputs
    if ( index < 0 and index >= len(parking_slot)):

        print("Parking slot index is out of range")
        return "Parking slot index is out of range"

    if ( parking_slot[index] == None):

        print("Slot number ", index + 1, " is already free")

    else:

        parking_slot[index] = None
        print("Slot number ", index + 1, " is free")

def status(parking_slot):

    print("Output (tab delimited output):")

    print("Slot No \tRegistration No. \tColour")

    # prints out parking status
    for index, each in enumerate(parking_slot):

        if (each == None):

            continue

        else:

            print(index + 1, each[1], each[2])

def registration_numbers_for_cars_with_colour(parking_slot, colour):

    for i, each in enumerate(parking_slot):

        if (each[0] == None):

            continue

        elif (each[2] == colour):

            print(each[1], end=" " )
    print()

def slot_numbers_for_cars_with_colour(parking_slot, colour):

    for i, each in enumerate(parking_slot):

        if (each[0] == None):

            continue

        elif (each[2] == colour):

            print(i + 1, end=" " )
    print()

def slot_number_for_registration_number(parking_slot, registry_no):

    for i, each in enumerate(parking_slot):

        if (each[0] == None):

            continue

        elif (each[1] == registry_no):

            print(i + 1, end=" " )

    return("Not Found")

def main():
    data = read_file("./file_inputs.txt")
    parking_slot = []
    for current in data:

        info = current[0]

        if (info == "create_parking_lot"):

            n = current[1]
            parking_slot = create_parking_slot(n)

        elif (info == "park"):

            parking_info = assign_parking(parking_slot, current)

            if (parking_info == -1):
                print("Sorry, parking lot is full")
            else:
                print("Allocated slot number: ", parking_info + 1)

        elif (info == "leave"):

            index = current[1]
            remove_parking(parking_slot, index)

        elif (info == "status"):
            status(parking_slot)

        elif (info == "registration_numbers_for_cars_with_colour"):
            colour = current[1]
            registration_numbers_for_cars_with_colour(parking_slot, colour)

        elif (info == "slot_numbers_for_cars_with_colour"):
            colour = current[1]
            slot_numbers_for_cars_with_colour(parking_slot, colour)

        elif (info == "slot_number_for_registration_number"):
            registry_no = current[1]
            slot_number_for_registration_number(parking_slot, registry_no)
        # print(current[1:])

# Unit testing
# Create a parking lot with 6 slot
# print("Create a parking lot with 6 slot ", len(create_parking_slot(6)) == 6)
# # Read the file inputs
# print("\'Read the file inputs\' ")
# for current in read_file("./file_inputs.txt"):
#     print current

main()
