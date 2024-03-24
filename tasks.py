global list

# Task 1
squares_list = [x**2 for x in range(1, 11)]
print("Task 1 - List Comprehensions:", squares_list)

# Task 2
def generate_squares(start, end):
    return [x**2 for x in range(start, end+1)]
print("Task 2 - Functions:", generate_squares(1, 10))

# Task 3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end+1)]
generator = SquareGenerator()
list = SquareGenerator.generate_squares(generator, 1,10)
print("Task 3 - Classes: "+str(list))

#Task 4
import math

class SquareGenerator:
    def generate_squares(self, start, end):
        return [math.sqrt(x) for x in list]
generator = SquareGenerator()
list = SquareGenerator.generate_squares(generator, 1, 10)
print("Task 4 - Libraries: " + str(list))

# Task 5
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start.")
        return [math.pow(x,2) for x in range(start,end+1)]
generator = SquareGenerator()
list = SquareGenerator.generate_squares(generator, 1, 10)
print("Task 5 - Exceptions: " + str(list))

from square_generator import SquareGenerator
generator = SquareGenerator()
list = generator.generate_squares(1, 10)
print("Task 6 - Modules: " + str(list))

# Task 8
class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start.")
        return [x**3 for x in range(start, end+1)]
generator = CubicGenerator()
list = generator.generate_cubes(1, 10)
print("Task 8 - Inheritance: " + str(list))

# Task 9
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start.")
        if start < end:
            return [x**2 for x in range(start, end+2)]
        else:
            raise ValueError("Start of the range must be less than or equal to end.")
generator = CubicGenerator()
list = generator.generate_squares(1, 10)
print("Task 9 - Function Overriding: " + str(list))

# Task 10
from abc import ABC, abstractmethod

class AbstractSquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

class SquareGenerator(AbstractSquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start.")
        return [math.pow(x,2) for x in range(start, end+10)]

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start.")
        if start < end:
            return [math.pow(x,3) for x in range(start, end+2)]
        else:
            raise ValueError("Start of the range must be less than or equal to end.")
generator = CubicGenerator()
list = generator.generate_squares(1, 10)
print("Task 10 - Abstract Elements: " + str(list))

