import unittest
from clifford import *
from clifford.g3c import *
from clifford.tools.g3c import *
from clifford.io import *


class TestBasicIO(unittest.TestCase):

    def test_write_and_read(self):
        file_name = "test.ga"

        basis_names = np.array(list(sorted(layout.basis_vectors.keys())), dtype=bytes)

        mv_array = ConformalMVArray([random_point_pair() for i in range(1000)]).value
        write_ga_file(file_name, mv_array, layout.metric, basis_names, compression=True,
                      transpose=False, sparse=False, support=False)

        data_array, metric_2, basis_names_2, support = read_ga_file(file_name)

        np.testing.assert_equal(data_array, mv_array)
        np.testing.assert_equal(layout.metric, metric_2)
        np.testing.assert_equal(basis_names, basis_names_2)

    def test_write_and_read_array(self):
        file_name = "test.ga"

        mv_array = MVArray([random_point_pair() for i in range(1000)])
        mv_array.save(file_name, compression=True, transpose=False, sparse=False, support=False)

        loaded_array = layout.load_ga_file(file_name)

        np.testing.assert_equal(loaded_array.value, mv_array.value)

if __name__ == '__main__':
    unittest.main()