def create_parking_slot(n):
    parking_slot = [None] * n
    return parking_slot

def read_file(file_name):
    with open(file_name, 'r') as data:
        for line in data:
            print(line.replace('\n', '').split(' '))
# Unit testing
# Create a parking lot with 6 slot
print("Create a parking lot with 6 slot ", len(create_parking_slot(6)) == 6)

print(read_file("./file_inputs.txt"))
