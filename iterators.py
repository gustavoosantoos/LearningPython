myList = [1, 3, 5, 7, 10]
myIterator = iter(myList);
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

class myIter:
    def __iter__(self):
        self.current = 0
        return self
    def __next__(self):
        if self.current < 30:
            self.current += 5
            return self.current
        else:
            raise StopIteration

myCustomIteratorObj = myIter()
myCustomIterator = iter(myCustomIteratorObj)
print(next(myCustomIterator))
print(next(myCustomIterator))
print(next(myCustomIterator))
print(next(myCustomIterator))
print(next(myCustomIterator))
print(next(myCustomIterator))
print(next(myCustomIterator))