import time
import threading

def cals_square(numbers):
    print("calculate square numbers")
    for num in numbers:
        time.sleep(0.2)
        print("sqaure: " , num*num)


def cals_cube(numbers):
    print("calculate cube numbers")
    for num in numbers:
        time.sleep(0.2)
        print("cube: " , num*num*num)

array = [2,3,8,9]
t = time.time()
t1 = threading.Thread(target=cals_square, args=(array,))
t2 = threading.Thread(target=cals_cube, args=(array,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : " , time.time()-t )
print("Hah.... i am done with all my work now!")