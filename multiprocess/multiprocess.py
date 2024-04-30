import time
import multiprocessing

def cals_square(numbers):
    for num in numbers:
        time.sleep(10)
        print("sqaure: " , num*num)


def cals_cube(numbers):
    for num in numbers:
        time.sleep(10)
        print("cube: " , num*num*num)

if __name__ == '__main__':
    array = [2,3,8,9]
    p1 = multiprocessing.Process(target=cals_square, args=(array,))
    p2 = multiprocessing.Process(target=cals_cube, args=(array,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("done...")