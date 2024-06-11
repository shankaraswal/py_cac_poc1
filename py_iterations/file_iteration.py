# Open the file
with open('py_iterations/test.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        print(line.strip())  # strip() removes the trailing newline character
