class SerialNumberedObject:
    count = 0

    def __init__(self):
        SerialNumberedObject.count += 1
        self.serial_number = SerialNumberedObject.count

    def get_serial_number(self):
        return self.serial_number


def main():
    obj1 = SerialNumberedObject()
    obj2 = SerialNumberedObject()
    obj3 = SerialNumberedObject()

    for i in (obj1, obj2, obj3):
        print(f'I am object number {i.get_serial_number()}')


main()
