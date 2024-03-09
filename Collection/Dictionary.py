tele={"John" : 123456789, "Dev": 987654321,"Evaa":147258369}

print(tele["Dev"])

tele["Dev"] = 8527419363

for phn in tele:
    print("Name : "+ phn + " number: " + str(tele[phn]))