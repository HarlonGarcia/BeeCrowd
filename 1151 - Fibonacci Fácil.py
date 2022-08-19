number = int(input())
firstValue = 0
secondValue = 1

for i in range(number):
    if (i == number -1):
        print(firstValue)
    else:
        print(firstValue, end=" ")

    value = firstValue + secondValue
    firstValue = secondValue
    secondValue = value
