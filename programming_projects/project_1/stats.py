'''
Cole W. Leavitt
CSC110
Programming Project 3
This program implements classes for calculating descriptive statistics on lists.
'''

class DescriptiveStatisticsCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def mean(self):
        total = sum(self.numbers)
        count = len(self.numbers)
        mean_value = total / count
        return round(mean_value, 2)

    def variance(self):
        mean_value = self.mean()
        total_squared_diff = sum((x - mean_value) ** 2 for x in self.numbers)
        count = len(self.numbers)
        variance_value = total_squared_diff / (count - 1)
        return round(variance_value, 2)

    def standard_deviation(self):
        variance_value = self.variance()
        standard_deviation = variance_value ** 0.5
        return round(standard_deviation, 2)

    def range(self):
        lowest = min(self.numbers)
        highest = max(self.numbers)
        range_value = highest - lowest
        return range_value

# Example usage
numbers = [12, 34, 56, 78, 90]
calculator = DescriptiveStatisticsCalculator(numbers)

print("Mean:", calculator.mean())
print("Variance:", calculator.variance())
print("Standard Deviation:", calculator.standard_deviation())
print("Range:", calculator.range())
