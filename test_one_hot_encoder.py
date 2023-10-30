import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_empty_fit_transform(self):
        self.assertRaises(TypeError, fit_transform)

    def test_fit_transform_equal(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(*cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_fit_transform_not_in(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(*cities)
        self.assertNotIn(('Saint-Petersburg', [1, 0, 0]), transformed_cities)

    def test_fit_transform_in(self):
        cities = ['Moscow', 'New York', 'London', 'Rome']
        rome = ('Rome', [1, 0, 0, 0])
        transformed_cities = fit_transform(*cities)
        self.assertIn(rome, transformed_cities)


if __name__ == '__main__':
    unittest.main()
