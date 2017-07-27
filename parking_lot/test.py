import unittest
from parking_lot import *

parking_lot = Parking_lot()

class TestParkingLotMethods(unittest.TestCase):

    # test create parking slot with valid input (2)
    def test_create_parking_slot(self):

        self.assertEqual(parking_lot.create_parking_slot("2"), [None] * 2)

    # test create parking slot with invalid input (-1)
    def test_create_parking_slot_invalid_input(self):

        self.assertEqual(parking_lot.create_parking_slot("-1"), "Please input a list greater or equal 2")

    # test create parking slot with invalid input ("b")
    def test_create_parking_slot_invalid_input_2(self):

        self.assertEqual(parking_lot.create_parking_slot("bruh"), "Please input a valid number/digits")

    # test assigning parking slot with available slots
    def test_assign_parking(self):

        parking_slot = parking_lot.create_parking_slot("6")
        self.assertEqual(parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1234", "Black"]), 0)

    # test assigning parking slot with non-available slots
    def test_assign_parking_2(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1234"]), -1)

    # test removing None slots, field that is already empty
    def test_remove_parking(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.remove_parking(parking_slot, 1), "Slot number 1 is free")

    # test removing existing slot, field that is currently occupied
    def test_remove_parking_2(self):

        parking_slot = parking_lot.create_parking_slot("2")
        self.assertEqual(parking_lot.remove_parking(parking_slot, 1), "Slot number 1 is already free")

    # test removing Non-existing slots, field that is out of range
    def test_remove_parking_3(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.remove_parking(parking_slot, 10), "Parking slot index is out of range")

    # test removing Non-existing slots, field that invalid (e.g alphabet)
    def test_remove_parking_4(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.remove_parking(parking_slot, "error now"), "Parking slot index is must be integer/digits/numbers")

    # test if status successfully executed
    def test_status(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.status(parking_slot), True)

    # test if registration numbers with existing colour
    def test_registration_numbers_for_cars_with_colour(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.registration_numbers_for_cars_with_colour(parking_slot, "Black"), True)

    # test if registration numbers with non-existing colour
    def test_registration_numbers_for_cars_with_colour_2(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.registration_numbers_for_cars_with_colour(parking_slot, "White"), False)

    # test if slot numbers with existing colour
    def test_slot_numbers_for_cars_with_colour(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.slot_numbers_for_cars_with_colour(parking_slot, "Black"), True)

    # test if slot numbers with non-existing colour
    def test_slot_numbers_for_cars_with_colour_2(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.slot_numbers_for_cars_with_colour(parking_slot, "White"), False)

    # test if slot numbers with registration number
    def test_slot_number_for_registration_number(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.slot_number_for_registration_number(parking_slot, "KH-AH-BB-1111"), "Found")

    # test if slot numbers with with non-registration number
    def test_slot_number_for_registration_number_2(self):

        parking_slot = parking_lot.create_parking_slot("2")
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-1111", "Black"])
        parking_lot.assign_parking(parking_slot, ["park", "KH-AH-BB-2222", "Black"])
        self.assertEqual(parking_lot.slot_number_for_registration_number(parking_slot, "KH-AH-BB-9999"), "Not Found")

    # test if the programe close and stop writing into new files
    @unittest.skip("demonstrating skipping for closing the program")
    def test_close_program(self):

        self.assertTrue(parking_lot.close() == True)

if __name__ == '__main__':
    unittest.main()
