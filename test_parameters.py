import unittest
from parameters import create_query


class ParametersTest(unittest.TestCase):
    def test_parameters(self):
        test_languages = ['JavaScript']
        test_stars = 1000

        self.assertEqual(create_query(test_languages, test_stars),
                         f"stars:>{test_stars} language:{test_languages[0]} ", "should equal")

        self.assertNotEqual(create_query(test_languages, test_stars),
                            f"stars:>{test_stars} language:{test_languages} ", "should not equal")


if __name__ == '__main__':
    unittest.main()
