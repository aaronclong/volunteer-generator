"""Unit Test to Confirm Trie Accuracy"""
import json
import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    """ Python test ment to run on saved copy of slack JSON data
    """
    def setUp(self):
        self.trie = Trie()
        #Default Slack JSON file name
        with open('users.json') as users:
            loaded = json.load(users)
            for member in loaded['members']:
                if 'real_name' not in member:
                    continue
                self.trie.add_name(0, member['real_name'].lower(),
                                   member)
    def test_addition(self):
        """ Making Sure trie entries are added correctly
        """
        added = self.trie.add('Jane Doe'.lower(), {'value': 0})
        self.assertTrue(added)
        self.assertIsNotNone(self.trie.search('Jane Doe'.lower()))
    def test_search(self):
        """ Verifying Trie entries
        """
        self.assertIsNone(self.trie.search('John Doe'.lower()))
        self.assertIsNotNone(self.trie.search('Aaron Long'.lower()))


if __name__ == '__main__':
    unittest.main()
