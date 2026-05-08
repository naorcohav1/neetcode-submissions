class DynamicArray:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity            


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size +=1 

    def popback(self) -> int:
        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -=1
        return value

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity
        new_arr[:self.size] = self.arr[:self.size]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity