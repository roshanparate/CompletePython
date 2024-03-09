
def calculate_total(listD):
    total = 0
    for bal in listD:
        total = total + bal
    return total

val_list = [12,13,45,46,78,79,10]

print(calculate_total(val_list))