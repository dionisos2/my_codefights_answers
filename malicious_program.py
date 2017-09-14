from utils import benchmark, testFunction
from datetime import datetime

def maliciousProgram(x):
    curDate, changes = x
    try:
        the_date = datetime.strptime(curDate, '%d %b %Y %H:%M:%S')
        # (d, m, Y, H, M, S) = (the_date.day, the_date.month, the_date.year, the_date.hour, the_date.minute, the_date.second)
        (Y, m, d, H, M, S,_ ,_ ,_) = the_date.timetuple()
        (d, m, Y, H, M, S) = (a+b for a,b in zip((d, m, Y, H, M, S), changes))
        the_date = datetime(Y, m, d, H, M, S)
        return the_date.strftime('%d %b %Y %H:%M:%S')
    except ValueError as e:
        return curDate

testCases = [
    (("01 Jul 2016 16:53:24", [2, 3, -1, 0, 5, 4]), "03 Oct 2015 16:58:28"),
    (("28 Jan 1900 16:09:10", [1, 1, 0, 5, 10, 15]), "28 Jan 1900 16:09:10")
]

testFunction(testCases, maliciousProgram, 'maliciousProgram')
