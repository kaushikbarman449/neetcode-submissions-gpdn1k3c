import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args):
        if len(args) == 1:
            radius = args[0]
            return round(math.pi * (radius ** 2), 2)
        
        if len(args) == 2:
            length, width = args
            return length * width
    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
