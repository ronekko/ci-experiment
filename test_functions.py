import unittest

import numpy as np

import functions


class TestSquare(unittest.TestCase):

    def test_scalar(self):
        x = 1
        y_desired = 1
        y_actual = functions.square(x)
        np.testing.assert_equal(y_desired, y_actual)


if __name__ == '__main__':
    unittest.main()
