import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_greet_world(self) -> None:
        self.assertEqual(greet("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
