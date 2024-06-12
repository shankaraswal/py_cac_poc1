
def num_skipper(start, end, skip_count):
    for i in range(start, end+1, skip_count):
        yield i
        
        
for num in num_skipper(10, 50, 3):
    print(num)