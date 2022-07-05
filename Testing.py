import unittest

class Testing(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3*4, 12, "3*4 Failure")

    def test_strings_a_4(self):
        self.assertEqual("a"*4, "aaaa", "a*4 Failure")


if __name__ == '__main__':
    unittest.main()






















# def get_circle_area(r):
#     return 3.14*r**2
#
# result = get_circle_area(3)
# print(result)



