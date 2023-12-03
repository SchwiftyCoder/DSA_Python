# // Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# //For Example:
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# //should return false.
# //-----------
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# //should return true.

# // 2 parameters - arrays - no size limit
# // return true or false

class Arrays:
    
    def __init__(self, list1, list2) -> None:
        self.dictionary = {} 
        self.list1 = list1
        self.list2 = list2
        

    def _buildDictionary(self):
        # create a dictionary out of the first array elements, values: boolean true
        for item in self.list1:
            self.dictionary[item] = True 

    def containsCommonItem(self):
        self._buildDictionary()
        print(self.list1)
        print(self.list2)
        # traverse the second array and check if it is in the diction keys
        for item in self.list2:
            if item in self.dictionary.keys():
                print("{} matches".format(item))
            else:
                print(f'{item} does not match')

list1 = ['a', 'b', 'c', 'x']
list2 = ['v', 'j', 'c', 'x']
list3 = ['c', 'x', 'a', 'd']

a = Arrays(list1, list3) 
a.containsCommonItem()