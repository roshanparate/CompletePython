book = {}

book["john"] = {
    "name" : "john",
    "address" : "1, high street, MH",
    "number" : 123456
}

book["dev"] = {
    "name" : "dev",
    "address" : "1, low street, MH",
    "number" : 654321
}

book["evaa"] = {
    "name" : "evaa",
    "address" : "1, mid street, MH",
    "number" : 987654
}

import json
s = json.dumps(book)

# write file
with open("c://Users//roshs//PycharmProjects//PythonAdvance//JsonInPython//book.txt","w") as f:
    f.write(s)

# read file
f = open("c://Users//roshs//PycharmProjects//PythonAdvance//JsonInPython//book.txt","r")
s = f.read()
print(s)

bJ= json.loads(s)
print(book)


for book in bJ:
    print(bJ[book])
