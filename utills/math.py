class Math:
    def __init__(self, *args):
        self.numbers = args

    def sum(self):
        return sum(self.numbers)

    def diff(self):
        difference = self.numbers[0]
        for x in self.numbers[1:]:
            difference = difference - x
        return difference

    def multiplication(self):
        multi = 1
        for x in self.numbers:
            multi = multi*x
        print(multi)
        
    def __str__(self):
        return f"Numbers: {self.numbers}"