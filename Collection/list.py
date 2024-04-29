number = [123,456,789,147,258,369]
even =[]

for num in number:
    print(num)

# get even number(by List comprehensions)
even =[i for i in number if i%2==0]
print(even)
