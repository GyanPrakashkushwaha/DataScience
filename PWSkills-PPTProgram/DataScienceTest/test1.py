"""## Question 17
17. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list.
 Use list comprehension to solve this problem."""

def evenLst(nums):
    even_nums = [i for i in nums if i%2 == 0]
    return even_nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(evenLst(nums))

