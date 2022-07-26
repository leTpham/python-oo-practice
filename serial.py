class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initialize with a start number"""
        self.start = start
        self.temp = self.start

    def __repr__(self):
        return f"I am {self.start} "

    def generate(self):
        """it return the next sequential number"""
        new_num = self.start
        self.start += 1
        return new_num

    def reset(self):
        """reset the number back to the original start number"""
        self.start = self.temp
