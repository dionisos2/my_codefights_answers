import time

def benchmark(func):
    """
        st decorator to calculate the total time of a func
    """

    def decoredFunc(*args, **keyArgs):
        t1 = time.time()
        r = func(*args, **keyArgs)
        t2 = time.time()
        print(f'Function={func.__name__}, Time={t2 - t1}')
        return r

    return decoredFunc
