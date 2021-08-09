"""
File: arraySortedBag.py
Author: James Lawson, Harrison Pinkerton, Laruie Jones
A tester program for bag implementations.
"""

from arrays import Array
from abstractBag import AbstractBag
import random

class ArraySortedBag(AbstractBag):
    """An array-based bag implementation."""


    # Class variables
    DEFAULT_CAPACITY = 25

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""
        
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    def __contains__ (self, item):
        """ implements a more efficient search algorithm"""
        #write this
        for self in self._items:
            if self == item:
                return True
        return False

    # Accessor Methods
    def __iter__(self):
        myModCount = self._modCount
        cursor = 0

        while cursor < len(self):
            yield self._items[cursor]
            if myModCount != self._modCount:
                raise AttributeError("Cannot modify!")
            cursor += 1

            

    def checkWord(self, word):
        score = -1
        print("Avaliable letters: " + scrabble)
        userWord = input("Make a word:")

        for i in userWord:
            contains(i, self._items)


            
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if other is self:
            return True
        if len(other) != len(self):
            return False
        if len(other) != len(self):
            return False
        if type(other) != type(self):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True


        

    # Mutator Methods

    def generate(v,c):
        
        self.clear()
        
        vowels = [a, e, i, o, u]
        consonants = [b, c, d, f, g, h, j, k ,l ,m ,n, p, q, r, s, t, v, w, x, y, z]

        scrabble = self._items
        print(self._items)
        
        for i in range(v):
            self._items = random.choice(vowels)
        print(self._items)

        for i in range(c):
            self._items = random.choice(consonants)
        print(self._items)


        
    
    def clear(self):
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        self._modCount += 1

    def add(self, item):
        # resize here if needed

        #print(self._items)
        
        if len(self._items) == len(self):
            self.grow()

        newIndex = len(self)

        for i in range(len(self)):
            if item <= self._items[i]:
                newIndex = i
                break
            
        for j in range(len(self), newIndex, -1):
            self._items[j] = self._items[j -1]
        self._items[newIndex] = item
        self._size += 1


    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        tIndex = 0
        for i in range(len(self._items)):
            if item == self._items[i]:
                tIndex = i
                break
            if i == len(self):
                raise IndexError("item is removed from self")
            
        for j in range(tIndex, len(self)-1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        if self._size < .25*len(self._items):
            self.shrink()

    def grow(self):
        """Doubles in size"""
        tempArray = Array(len(self) * 2)
        for i in range(len(self)):
            tempArray[i] = self._items[i]
        self._items = tempArray
        pass

    def shrink(self):
        """Becomes half the current size, does not become smaller than
             initial capacity."""
        half = int(len(self._items) / 2)
        halfArray = Array(half)
        if half > ArraySortedBag.DEFAULT_CAPACITY:
            for i in range(len(self)):
                halfArray[i] = self._items[i]
            self._items = halfArray
        else:
            pass

        

def main():
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k" ,"l" ,"m" ,"n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    scrabble = ArraySortedBag.DEFAULT_CAPACITY
    scrabble = str(scrabble)

    print(scrabble)
        
    for i in range(10):
        scrabble += random.choice(vowels)
    print(scrabble)

    for i in range(15):
        scrabble += random.choice(consonants)
    print(scrabble)

    scrabble = scrabble.replace("25", "")
    
    score = -1
    print("Avaliable letters: " + scrabble)
    userWord = input("Make a word:")
    initialLen = userWord

    winner = False
    sL = 0
    for i in range(10000):
        if len(userWord) == 0:
            winner = True
            break
        else:
            if userWord[0] in scrabble[sL]:
                scrabbleLen = len(scrabble)
                #scrabble = scrabble[:i] + scrabble[i+1:]
                userWord = userWord[:0] + userWord[1:]
                print(scrabble)
                print(userWord)
                sL = 0
            else:
                if sL > 23:
                    winner = False
                    break
                else:
                    sL +=1
    
                

##    winner = True
##    for i in range(25):
##        if userWord in scrabble:
##            winner = True
##        else:
##            winner = False
    

##    for i in range(25):


    if winner == False:
        print("You can't make that word with those letters, you lose!")
    if winner == True:
        print("You scored the following points!")
        print(len(initialLen))


    #for i in userWord:
        #contains(i, self._items)






    #ihatescrabble = ArraySortedBag.generate(10, 5)
    #return ihatescrabble

if __name__ == "__main__":
    main()
##    a = ArrayBag()
##    b = ArrayBag(["a", "b", "c"])
##
##    a.add("hi")
##    a.add("bye")
##    a.add("cat")
##
##    print(a)
##    print(type(a + b))
##
##    a2 = ArrayBag(a)
##    print(a2)
##
##    for item in a:
##        print(item)
##
##    a.clear()
##    print(a)
