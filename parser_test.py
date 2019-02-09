import ast
import unittest
from hello_world_python import *

class ParserTest(unittest.TestCase):
    def test_hello_world(self):
        parser = Analyzer("def hello():\n  return \"Hello, World!\"")
        self.assertEqual(parser.analyzeSolution(), True)

    def test_goodbye_world(self):
        parser = Analyzer("def hello():\n  return \"Goodbye, World!\"")
        self.assertEqual(parser.analyzeSolution(), False)


if __name__ == '__main__':
    unittest.main()
