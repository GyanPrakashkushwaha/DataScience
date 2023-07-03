
"""
## Question 19
 Write a function called ‘calculate_mean’ that takes a list of numbers as input and returns the mean (average) of the numbers.
 The function should calculate the mean using the sum of the numbers divided by the total count."""

def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data = [10, 15, 20, 25, 30]
mean_value = calculate_mean(data)
print(mean_value)
