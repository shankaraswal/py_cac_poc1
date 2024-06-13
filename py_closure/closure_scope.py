def multipliWith(num1):
    def multipliNumber(num2):
        return num1 * num2
    return multipliNumber


multipliWith5 = multipliWith(5)
multipliWith10 = multipliWith(8)

print(multipliWith5(5))
print(multipliWith10(2))