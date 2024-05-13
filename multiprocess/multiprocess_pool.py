from multiprocessing import Pool
import time

def f(n):
    sum =0;
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":
    t1= time.time()
    # Pool use all core of CPU to process operation
    p = Pool()

    # p = Pool(processes=3)-- it will create only 3 processes
    result = p.map(f, range(100000))
    p.close()
    p.join()

    print("pool took : ", time.time()-t1)

    t2 = time.time()
    result =[]
    for x in range(100000):
        result.append(f(x))

    print("serial process took : ",time.time() - t2)