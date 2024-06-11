start_num= 3
end_num = 97
arr= []

for num in range(start_num, end_num+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            arr.append(num)
print (arr)