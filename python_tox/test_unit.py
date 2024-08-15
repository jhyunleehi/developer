import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_1(self):
        c=add(1, 2)
        self.assertEqual(c, 3)

    def test_add_2(self):
        c=add(1, 2)
        self.assertEqual(c, 3)

# if __name__ == '__main__':
#     unittest.main()