class Arrays:

    # creates an aray object of size 0
    def __init__(self) -> None:
        self.length = 0
        self.data = []

    # get element at specified index
    def get(self, index):
        if(index > self.length):
            return None
        return self.data[index]
    
    # return size of array
    def getSize(self):
        return self.length
    
    # add element to array
    # None here is used as a list to signify absence of a value
    def add(self, element):
        scale_factor = 1
        if(self.length == len(self.data)): # checks if the array is full
            self.data += [None] * scale_factor # concatenates self.data with a list type of size 10 and elemenst being None
        self.data[self.length] = element
        self.length += 1

    # remove element at specified index
    def removeAt(self, index):
        if (self.get(index) != -1):
            del self.data[index]
            self.length -= 1

    # remove first occurence of element 
    def remove(self, element): 
        index = self.contains(element)
        if index != -1:
            self.removeAt(index)
        

    # check if array contains element 
    # returns the first index occurence if it exists
    def contains(self, element): 
        for index in range(0, self.length):
            if(self.data[index] == element):
                return index
        return -1
    
    def __str__(self) -> str:
        return f"{self.data}"
    

# script only runs if it is the main module, i.e not imported as a module
# if this script were inported into another application, it won't run the code below
if __name__ == '__main__': 
    arr1 = Arrays()
    index = 10
    print("array: ", arr1) 
    print(f"{arr1.contains(213)}")
    arr1.add(23)
    print("array: ", arr1) 
    arr1.add(21)
    print("array: ", arr1) 
    print(f"{arr1.contains(213)}")
    arr1.removeAt(0)
    print(arr1)
    arr1.remove(21)
    print(arr1)

