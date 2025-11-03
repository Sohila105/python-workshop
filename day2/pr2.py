class CustomRange:
    def __init__(self, start, end= None , step=1):
        if end is None:
            self.start = 0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.end:
            raise StopIteration
        elif self.step < 0 and self.current <= self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

    def reset(self):
        self.current = self.start


class EvenNumbers(CustomRange):
    def __init__(self, start, end):
        super().__init__(start, end, 1)

    def __next__(self):
        while True:
            value = super().__next__()
            if value % 2 == 0:
                return value
            

for num in CustomRange(10):
    print(num)

for num in EvenNumbers(1, 20):
    print(num)