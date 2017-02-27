"""Trie implementation"""
class Trie:
    """ Try structure to help sort users more quickly
        Will hold a list with 27 indexes
        a-z will start and end from 0-25
        The 27th index (26) will be space indicating the seperation between firt and last names
    """
    def __init__(self):
        self.children = {}
        self.value = None
    def add_index(self, letter):
        """ Add an index to the current node
        """
        if letter not in self.children:
            self.children[letter] = Trie()
        return self.children[letter]
    def add_nam(self, index, name, obj):
        """ Recursive name addition
            names must be in lower case though
        """
        if index > len(name):
            return False
        if name.islower() is False:
            raise Exception('Names must be in lower case')
        letter = ord(name[index])
        ref = self.add_index(letter) #reference next trie node in the range
        if index == len(name):
            ref.value = obj
            return True
        return ref.add_name(index+1, name, obj)
    def search(self, name):
        """ Search Trie
            names must be in lower case though
            Returns False if doesn't exist
            Returns stored object once the base is found
        """
        if name.islower():
            cur = self #curser for node traversal
            for letter in name:
                num = ord(letter)
                if num not in cur.children:
                    return False
                cur = cur.children[cur]
            return cur.value
