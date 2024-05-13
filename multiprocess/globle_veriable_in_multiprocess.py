import multiprocessing

def cals_square(numbers, result, v, q):
    v.value = 5.6;
    for inx, num in enumerate(numbers):
        result[inx] = num*num
        q.put(num*num)


if __name__ == '__main__':
    array = [2,3,8,9]
    #Globle veriable declearation as array
    result = multiprocessing.Array('i',4)

    # Globle veriable declearation as value
    v = multiprocessing.Value('d', 0.0)

    # Globle veriable declearation as Queue
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=cals_square, args=(array, result, v, q))

    p1.start()
    p1.join()

    print("done...")
    print(result[:])
    print(v.value)

    while q.empty() is False:
        print(q.get())