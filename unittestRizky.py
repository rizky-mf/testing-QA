import unittest

symbols = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
            ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

def romannumeral(number):
    outstring = ""
    while number > 0:
        for symbol, value in symbols:
            if number - value >= 0:
                outstring += symbol
                number = number - value
                break
    return outstring
    

class Test(unittest.TestCase):
    def test_9(self):
        self.assertEqual(romannumeral(9), "IX")
    def test_29(self):
        self.assertEqual(romannumeral(29),"XXIX")
    def test_707(self):
        self.assertEqual(romannumeral(707), "DCCVII")
    def test_1800(self):
        self.assertEqual(romannumeral(1800),"MDCCC")

if __name__ == '__main__':
    number_in = raw_input("Enter a number: ")
    romannumeral(int(number_in))