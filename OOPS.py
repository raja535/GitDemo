class Calculator:
    num1 = 100
    num2 = 200

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("i am called automatically when object create")


    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num2 + Calculator.num1


obj = Calculator(3, 4)
obj.getData()
print(obj.Summation())

