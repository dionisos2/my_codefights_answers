from utils import benchmark, testFunction
from urllib.parse import urlparse, parse_qs
from itertools import takewhile

# def parseQuery(query):
#     return {key_value.split('=')[0]:key_value.split('=')[1] for key_value in query.split('&')} if query else {}

def urlSimilarity(x):
    url1, url2 = x

    url1 = urlparse(url1)
    url2 = urlparse(url2)
    result = 0

    result += 5 if url1.scheme == url2.scheme else 0
    result += 10 if url1.netloc == url2.netloc else 0
    result += len(list(takewhile(lambda x:x[0]==x[1], zip(url1.path.split('/'), url2.path.split('/'))))) - 1
    query1 = parse_qs(url1.query)
    query2 = parse_qs(url2.query)
    for key in query1:
        if key in query2:
            result += 2 if query1[key] == query2[key] else 1
    return result



testCases = [
    (("https://codefights.com/home/test?param1=42&param3=testing&login=admin", "https://codefights.com/home/secret/test?param3=fish&param1=42&password=admin"), 19),
    (("https://codefights.com/home/test?param1=42&param3=testing&login=admin", "http://codefights.org/about?42=param1&tesing=param3&admin=login"), 0)
]

testFunction(testCases, urlSimilarity, 'urlSimilarity')
