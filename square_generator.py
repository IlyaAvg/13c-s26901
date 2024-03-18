# Task 6
import math
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start.")
        return [math.sqrt(x) for x in range(start, end+1)]