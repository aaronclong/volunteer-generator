import unittest
from .trie import Trie

class TestTrie(unittest.TestCase):
    """ Python test ment to run on saved copy of slack JSON data
    """
    def setUp(self):
        self.trie = Trie()

if __name__ == '__main__':
    unittest.main()