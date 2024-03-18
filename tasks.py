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

list = SquareGenerator.generate_squares(SquareGenerator, 1,10)
print("Task 3 - Classes: "+str(list))