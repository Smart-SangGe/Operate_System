import unittest
import a


class TestGenChar(unittest.TestCase):
    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            a.GenChar(10, -1)

    def test_length_of_list(self):
        length = 10
        N = 30
        result = a.GenChar(length, N)
        self.assertEqual(len(result), length)

    def test_elements_in_range(self):
        length = 10
        N = 30
        result = a.GenChar(length, N)
        for item in result:
            self.assertTrue(0 <= item < N)


if __name__ == "__main__":
    unittest.main()
