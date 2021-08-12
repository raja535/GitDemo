from OOPS import Calculator


class Childimp(Calculator):

    num3 = 300

    def __init__(self):
        Calculator.__init__(self, 2, 5)

    def getCompleteData(self):
        return self.num3 + self.num1 + self.Summation()

obj1 = Childimp()
print(obj1.getCompleteData())

