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

def testFunction(testCases, func, funcName):
    for testCase in testCases:
        result = func(testCase[0])
        desiredResult = testCase[1]
        if result != desiredResult:
            print('-'*50)
            print('with X = ' + str(testCase[0]))
            print()
            funcStr = funcName + '(X)'
            print(funcStr + " should be " + str(desiredResult))
            print()
            print(funcStr + ") = " + str(result))
        else:
            print('.', end='')

    print('')
