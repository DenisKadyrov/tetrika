import unittest
from solution import strict 


@strict
def sum_num(a: int, b: int) -> int:
    return a + b

@strict
def concatenate_str(a: str, b: str) -> str:
    return a + b


class TestDecorator(unittest.TestCase):

    def test_with_correct_types(self):
        self.assertEqual(sum_num(1, 4), 5)
        self.assertEqual(sum_num(2, 10), 12)

        self.assertEqual(concatenate_str("Hi! ", "How are u?"), "Hi! How are u?")
        self.assertEqual(concatenate_str("Hello", ", World"), "Hello, World")

    def test_with_incorrect_types(self):
        with self.assertRaises(TypeError):
            sum_num(1, 2.8)

        with self.assertRaises(TypeError):
            sum_num(1, "3")

        with self.assertRaises(TypeError):
            sum_num(2.4, "3")

        with self.assertRaises(TypeError):
            sum_num("3", 3)

        with self.assertRaises(TypeError):
            concatenate_str("a", 3)

        with self.assertRaises(TypeError):
            concatenate_str(5, "ch")

        with self.assertRaises(TypeError):
            concatenate_str(5, 4)

if __name__ == "__main__":
    unittest.main()
