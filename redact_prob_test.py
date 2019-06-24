import unittest
from redact_prob import redact

class RedactTest(unittest.TestCase):

    def test_redact_func(self):
        arr_one = ['one', 'two', 'three']
        arr_two = ['two', 'four', 'six']
        new_arr = []

        new_arr = redact(arr_one, arr_two)
        assert new_arr == ['one', 'three']

        arr_one = ['a', 'b', 'c']
        arr_two = ['a', 'b', 'c']
        new_arr = []

        new_arr = redact(arr_one, arr_two)
        assert new_arr == []

        arr_one = []
        arr_two = []
        new_arr = []

        new_arr = redact(arr_one, arr_two)
        assert new_arr == []

        arr_one = ['one', 'one', 'one', 'trex', 'bubble']
        arr_two = ['trex', 'building', 'dog', 'foo']
        new_arr = []

        new_arr = redact(arr_one, arr_two)
        assert new_arr == ['one', 'one', 'one', 'bubble']

if __name__ == '__main__':
    unittest.main()
