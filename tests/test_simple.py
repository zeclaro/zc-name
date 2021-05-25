# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import zcname


class TestSimple(unittest.TestCase):

    def test_get_full_name(self):
        # self.assertEqual(add_one(5), 6)
        rest_client = zcname.app.AppRestClient()
        self.assertIsNotNone(rest_client.get_full_name())


if __name__ == '__main__':
    unittest.main()
