# Example of using an iterator with a list
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)

print(next(my_iterator))  # Outputs: 1
print(next(my_iterator))  # Outputs: 2
print(next(my_iterator))  # Outputs: 3
print(next(my_iterator))  # Outputs: 4
# print(next(my_iterator))  # Raises StopIteration as there are no more elements
