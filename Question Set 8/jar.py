class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = str(int(self.size) * "🍪")
        return cookies

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity != 12:
            raise ValueError("Capacity must be 12")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > 12:
            raise ValueError("There are too many/little cookies!")
        else:
            self._size = size


jar = Jar()
jar.deposit(12)
jar.withdraw(1)
print(jar)
