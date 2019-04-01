class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current = 0
            return r
        else:
            return StopIteration


a, b, c = Counter(3)
print(a, b, c)
