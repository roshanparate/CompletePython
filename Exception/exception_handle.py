try:
    # num = 10/0
    number1 = int(input("Enter number1 : "))
    number2 = int(input("Enter number2 : "))
    print(number1/number2)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print("Invalid Value..")