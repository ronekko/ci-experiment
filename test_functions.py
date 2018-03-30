import unittest

import numpy as np

import functions


class TestSquare(unittest.TestCase):

    def check_square(self, x, y_desired):
        y_actual = functions.square(x)
        np.testing.assert_equal(y_desired, y_actual)

    def test_scalar(self):
        x = 1
        y_desired = 1
        self.check_square(x, y_desired)

    def test_ndarray(self):
        x = np.array([0, 1, 2, 3], dtype=np.float32)
        y_desired = np.array([0, 1, 4, 9], dtype=np.float32)
        self.check_square(x, y_desired)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            functions.square('a')


if __name__ == '__main__':
    unittest.main()
