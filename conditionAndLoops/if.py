indian = ["samosa", "panipuri", "poha", "dal", "gulabjamun"]
italian = ["pizza", "pasta","risotto"]
japanese = ["sukiyaki","unagi","donburi","sushi"]

dish= input("Enter dish name:")

if dish in indian:
    print("Indian Dish")
elif dish in italian:
    print("Italian Dish")
elif dish in japanese:
    print("Japanese Dish")
else:
    print("Dish not register to our database")