numbers = [123, 456, 789, 321, 654, 987, 147, 258, 369, 741, 852, 963]

total = 0
for num in numbers:
    total = total +num
print(total)


for i in range(1, 11):
    print(i*i)

total = 0
for index in range(len(numbers)):
    print('index: ', (index+1), 'value: ', numbers[index])
    total = total + numbers[index]
print(total)