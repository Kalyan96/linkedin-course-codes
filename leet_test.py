class MyHashSet(object):
    hash =[]
    def __init__(self):
        self.hash = []


    def add(self, key):
        if self.contains(key ) == False:
            self.hash.append(key)
        """
        :type key: int
        :rtype: None
        """

    def remove(self, key):
        if self.contains(key):
            self.hash.pop(self.hash.index(key))
        """
        :type key: int
        :rtype: None
        """

    def contains(self, key):
        for i in self.hash :
            if i == key :
                return True
        return False
        """
        :type key: int
        :rtype: bool
        """

