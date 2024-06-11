arr = [3, 0, 4, 1, 3, 2, 9, 5, 7, 0, 6, 5, 4, 2, 8, 1, 9, 6, 7, 3]

uniqe_arr = set()

for num in arr:
    if num in uniqe_arr:
        print(num, "is duplicate")
        continue
    else:
        uniqe_arr.add(num)
        
print('UNIQUE ITEM LIST IN ARR:', uniqe_arr)