"""
implementing a hastable class
underlying data structure: arrays
handling collisins
retriving elements
searching elements
deleting elements
"""
from typing import List


class HashTable:
    HASH_TABLE_MAX_SIZE = 50

    # creates a fized sized array that is used to store our key/value pairs
    # each array element is an array that stores the key value pair.
    # this helps to handle collision issues
    # actual elements are stored as a tuple paur like so (key, value)
    def __init__(self) -> None:
        self.hashtable = [[None] * self.HASH_TABLE_MAX_SIZE ]

    # the hash function to determine the index where our data will be stored
    """
    1. Iterate over the key string, character by character
    2. Convert each character to a number using Python's built-in ord function.
    3. Add the numbers for each character to obtain the hash for the entire string
    4. Take the remainder of the result with the size of the data list

    returns a value between 0 and (hashTableSize - 1)
    """
    def generateHash(self, key) -> int:
        hash = 0
        charSum = 0
        for char in key:
            charSum += ord(char)

        hash = charSum % self.HASH_TABLE_MAX_SIZE
        return hash

    # insertion operation
    """
        each index of the hastable stores a tuple pair. 
    """
    def insert(self, keyToAdd, value):
        hash = self.generateHash(keyToAdd)
        # iterate through the hashmap using the generated hash
        for hashKey, (keyInMap, _) in enumerate(self.hashtable[hash]):
            # if the key to add is found in the hashmap, then create a new tuple entry for it
            if keyInMap == keyToAdd:
                self.hashtable[hash][hashKey] = (keyToAdd, value)
        self.hashtable[hash].append((keyToAdd, value))

    # delete operation
    def delete(self, key):
        pass

    # search operation
    """
    Note: 
        hash_table[hashkey] returns a list of key, value tuple pairs
    """
    def search(self, keyToFind):
        hashKey = self.generateHash(keyToFind)
        for k, v in self.hashtable[hashKey]:
            if k == hashKey:
                return v
        return None

    # return all keys as a list
    """
    return only keys where elements are not none
    """
    def keys(self) -> List:
        return self.hashtable

    # returns all values
    def values(self) -> List:
        pass

    # return a key, value pair tuple as a list
    def keyValuePair(self) -> List:
        pass

    # print hasmap
    def __str__(self) -> str:
        dict = "{"
        for key, value in keyValuePair():
            dict += f"{key}: {value}, "

        return dict + "}"


hashtable = HashTable()
print(hashtable.generateHash(""))