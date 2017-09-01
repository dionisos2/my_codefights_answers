# https://codefights.com/arcade/python-arcade/yin-and-yang/ynSRuyh93ZffkPjtv

def rightBrother(number):
    a, b = number
    # parent = a/b → leftChild = a/(a+b) → b = a+b-a
    b = b - a
    # rightChild = (a+b)/b
    a = a + b
    return [a, b]

def parent(number):
    a, b = number
    # parent = a/b → rightChild = (a+b)/b → a = a+b-b
    return [a - b, b]

def leftChild(number):
    a, b = number
    return [a, a+b]

def bruteForce():
    a, b = 1, 1
    while 1:
        yield [a, b]
        if a < b: # left node → right node
            a, b = rightBrother([a, b])
        else:
            depth = 0
            while a > b:
                a, b = parent([a, b])
                depth += 1
            if a != b: # not at root
                a, b = rightBrother([a, b])
            else:
                depth += 1
            for i in range(depth):
                a, b = leftChild([a, b])


def compactBruteForce():
    a, b = 1, 1
    while 1:
        yield [a, b]
        if a < b:
            a, b = b, b - a
        else :
            depth = 0
            while a > b:
                a, b = [a - b, b]
                depth += 1
            if a != b:
                a, b = b, b - a
            else:
                depth += 1
            for i in range(depth):
                a, b = a, a+b


def calkinWilfSequence(number):
    sequence = compactBruteForce()

    result = 0
    while next(sequence) != number:
        result += 1
    return result


testCases = [
    ([1, 3], 3),
    ([1, 1], 0),
    ([3, 1], 6),
    ([14, 3], 110),
    ([7, 13], 129),
]


for testCase in testCases:
    print("calkinWilfSequence("+str(testCase[0])+") should be " + str(testCase[1]))
    print("calkinWilfSequence("+str(testCase[0])+") = " + str(calkinWilfSequence(testCase[0])))
