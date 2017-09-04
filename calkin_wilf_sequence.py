# https://codefights.com/arcade/python-arcade/yin-and-yang/ynSRuyh93ZffkPjtv

from utils import benchmark, testFunction


# def calkinWilfSequence(number):
#     def fractions():
#         ...

#     gen = fractions()
#     res = 0
#     while next(gen) != number:
#         res += 1
#     return res


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

def avoidLoop():
    a, b = 1, 1
    while 1:
        yield [a, b]
        if a < b:
            a, b = b, b - a
        else :
            depth = a//b
            a = a%b
            if a != b:
                a, b = b, b - a
            else:
                depth += 1
            b += depth * a


def avoidConditional():
    a, b = 1, 1
    while 1:
        yield [a, b]
        a, b = (b, b + a - 2*(a%b))


def calkinWilfSequence(number, sequence = None):
    if sequence == None:
        sequence = avoidConditional()
    result = 0
    while next(sequence) != number:
        result += 1
    return result


def calkinWilfSequenceQuick(number):
    if number == [1, 1]:
        return 0

    path = ''
    a, b = number
    while [a, b] != [1, 1]:
        if a < b:
            b -= a
            path += '0'
        else:
            a -= b
            path += '1'
    # 1+2+4+8+…+2^(n-1) = (2^n-1)/(2-1)=2^n-1
    addForDepth = 2**len(path)-1

    return addForDepth + int(path[::-1], 2)


testCases = [
    ([1, 3], 3),
    ([1, 1], 0),
    ([3, 1], 6),
    ([14, 3], 110),
    ([7, 13], 129),
]


testFunction(testCases, calkinWilfSequence, 'calkinWilfSequence')
@benchmark
def testWithSequence(func):
    calkinWilfSequence([1, 20], func())

testWithSequence(bruteForce)
testWithSequence(compactBruteForce)
testWithSequence(avoidLoop)
testWithSequence(avoidConditional)
benchmark(calkinWilfSequenceQuick)([1, 20])
