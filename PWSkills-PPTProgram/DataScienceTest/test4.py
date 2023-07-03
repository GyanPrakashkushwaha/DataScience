
""" ## Question 20.
 Write a function called ‘perform_hypothesis_test’ that takes two lists of numbers as input, representing two samples.
   The function should perform a two-sample t-test and return the p-value. Use the ‘scipy.stats’ module in Python to calculate the t-test and p-value.
"""


from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value

sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]
p_value = perform_hypothesis_test(sample1, sample2)
print(p_value)
