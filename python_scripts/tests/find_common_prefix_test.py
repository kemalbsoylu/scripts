import unittest

from python_scripts.find_common_prefix import find_common_prefix


class FindCommonPrefixTest(unittest.TestCase):
    def test_short_prefix(self):
        self.assertEqual(find_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_prefix_item(self):
        self.assertEqual(find_common_prefix(["camp", "campaign", "campfire", "campsite"]), "camp")

    def test_empty_string(self):
        self.assertEqual(find_common_prefix([""]), "")

    def test_empty_string_with_other_items(self):
        self.assertEqual(find_common_prefix(["", "rohan", "rohirrim"]), "")

    def test_no_prefix(self):
        self.assertEqual(find_common_prefix(["earth", "water", "air", "fire"]), "")

    def test_single_item(self):
        self.assertEqual(find_common_prefix(["one"]), "one")

    def test_type_error_in_the_list(self):
        with self.assertRaises(ValueError) as err:
            find_common_prefix([123, "morgul", "morgoth"])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Input must be a list of strings.")

    def test_input_type_error(self):
        with self.assertRaises(ValueError) as err:
            find_common_prefix(("morgul", "morgoth"))
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Input must be a list of strings.")

    def test_empty_list_is_an_error(self):
        with self.assertRaises(ValueError) as err:
            find_common_prefix([])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Empty lists are not allowed. Expecting list of strings.")


if __name__ == "__main__":
    unittest.main()
