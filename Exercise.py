expense_list = [2340, 2500, 2100, 3100, 2980]

expense = input("enter expense: ")
expense = int(expense)

if expense == expense_list[0]:
    print("Jan")
elif expense == expense_list[1]:
    print("Feb")
elif expense == expense_list[2]:
    print("Mar")
elif expense == expense_list[3]:
    print("April")
elif expense == expense_list[4]:
    print("May")
else:
    print(expense)

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)
