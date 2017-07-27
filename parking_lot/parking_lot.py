from __future__ import print_function

# global variable for writing each statement into STDOUT.txt
stdout = open("STDOUT.txt", "w")

class Parking_lot:

    def __init_(self):
        pass

    def create_parking_slot(self, n):

        try:
            n = int(n)

        # Verify if input is an integer/number/digits
        except ValueError:
            return "Please input a valid number/digits"

        # Verify if input is at least 2 inputs
        if (n < 2):
            stdout.write("Please input a list greater or equal 2\n")
            return "Please input a list greater or equal 2"

        # create parking slot list and return the list
        parking_slot = [None] * n
        stdout.write("Created a parking lot with " + str(len(parking_slot)) + " slots\n")
        return parking_slot

    def assign_parking(self, parking_slot, current_car):

        # looping through the parking slot to find a slot for current car
        for each_slot in range(len(parking_slot)):
            # if slot is empty, successfully allocated to a slot then return index of the allocated slot
            if (parking_slot[each_slot] == None):

                parking_slot[each_slot] = current_car
                stdout.write("Allocated slot number: " + str(each_slot + 1) + "\n")
                return each_slot

        # if no slots are available return -1
        stdout.write("Sorry, parking lot is full\n")
        return -1

    def remove_parking(self, parking_slot, index):

        try:

            index = int(index) - 1
            # Verify if input is at least 2 inputs
            if ( index < 0 and index >= len(parking_slot)):

                print("Parking slot index is out of range")
                stdout.write("Parking slot index is out of range\n")
                return "Parking slot index is out of range"


            if ( parking_slot[index] == None):

                print("Slot number ", index + 1, " is already free")
                stdout.write("Slot number " + str(index + 1) + " is already free\n")
                return "Slot number " + str(index + 1) + " is already free"

            else:

                parking_slot[index] = None
                print("Slot number ", index + 1, " is free")
                stdout.write("Slot number " + str(index + 1) + " is free\n")
                return "Slot number " + str(index + 1) + " is free"

        # catch error if index is out of range
        except IndexError:
            return "Parking slot index is out of range"

        # Verify if input is an integer/number/digits
        except ValueError:
            return "Parking slot index is must be integer/digits/numbers"

    def status(self, parking_slot):

        print("Output (tab delimited output):")
        stdout.write("Output (tab delimited output):" + "\n")

        print("Slot No \tRegistration No. \tColour")
        stdout.write("Slot No \tRegistration No. \tColour" + "\n")

        # prints out parking status
        for index, each in enumerate(parking_slot):

            if (each == None):
                # if each is None then skip to next element
                continue

            else:

                print(index + 1, each[1], each[2])
                stdout.write(str(index + 1) + " " + str(each[1]) + " " + str(each[2]) + "\n")

        return True

    def registration_numbers_for_cars_with_colour(self, parking_slot, colour):

        count = 0
        newString = []

        for i, each in enumerate(parking_slot):

            if (each[0] == None):
                # if each is None then skip to next element
                continue

            elif (each[2] == colour):

                # print(each[1], end=" " )
                newString.append(each[1])
                count += 1
                # stdout.write(str(each[1]) + " " )

        print (", ".join(newString))
        stdout.write(", ".join(newString))
        stdout.write("\n" )

        if (count == 0):

            return False

        else:

            return True

    def slot_numbers_for_cars_with_colour(self, parking_slot, colour):

        count = 0
        newString = []

        for i, each in enumerate(parking_slot):

            if (each[0] == None):
                # if each is None then skip to next element
                continue

            elif (each[2] == colour):

                # print(i + 1, end=", " )
                newString.append(str(i + 1))
                count += 1
                # stdout.write(str(i + 1) + " " )

        print (", ".join(newString))
        stdout.write(", ".join(newString))
        stdout.write("\n" )

        if (count == 0):

            return False

        else:

            return True

    def slot_number_for_registration_number(self, parking_slot, registry_no):

        count = 0
        newString = []

        for i, each in enumerate(parking_slot):

            if (each[0] == None):
                # if each is None then skip to next element
                continue

            elif (each[1] == registry_no):

                # print(i + 1, end=" " )
                newString.append(str(i + 1))
                count += 1
                # stdout.write(str(i + 1) + " " )

        # if no item match then return Not Found
        if (count == 0):

            print("Not Found")
            stdout.write("\nNot Found")
            return "Not Found"

        else:

            print (", ".join(newString))
            stdout.write(", ".join(newString))

    def close(self):

        # close the file to be written into STDOUT.txt
        stdout.close()
        return True
