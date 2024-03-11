
# w - write
# r - read
# a - append
# w+ - write and read file (new file will create if not exist)
# r+ - write and read file (new file will not create if not exist)

# write in file
f = open("c://Users//roshs//PycharmProjects//PythonAdvance//Files//fun.txt","a")
f.write("I love Python\n")
f.close()


# read file
r = open("c://Users//roshs//PycharmProjects//PythonAdvance//Files//fun.txt","r")
f_out = open("c://Users//roshs//PycharmProjects//PythonAdvance//Files//fun_out.txt","a")
for line in r:
    tokens = line.split(' ')
    f_out.write(line + " wordcount: " + str(len(tokens)) +"\n")
f_out.close()
r.close()

with open("c://Users//roshs//PycharmProjects//PythonAdvance//Files//fun_out.txt","r") as f:
    print(f.read())
