# https://codefights.com/arcade/python-arcade/picturing-the-parsibilities/pTZqFk8awghQba4ba

from utils import benchmark, testFunction
from collections import OrderedDict
import json

def createDefault(command):
    if isinstance(command, (int, float)):
        return 0
    if isinstance(command, str):
        return ''
    if isinstance(command, list):
        return []
    if isinstance(command, dict):
        return OrderedDict((name, createDefault(value)) for name, value in command.items())


def buildCommand(jsonFile):
    command = json.loads(jsonFile, object_pairs_hook=OrderedDict)
    return json.dumps(createDefault(command))








testCases = [
    ("{\"version\": \"0.1.0\",\"command\": \"c:python\",\"args\": [\"app.py\"],\"problemMatcher\": {\"fileLocation\": [\"relative\", \"${workspaceRoot}\"],\"pattern\": {\"regexp\": \"^(.*)+s$\", \"message\": 1}}}",
     "{\"version\": \"\", \"command\": \"\", \"args\": [], \"problemMatcher\": {\"fileLocation\": [], \"pattern\": {\"regexp\": \"\", \"message\": 0}}}"
    ),
    ("{}",
     "{}"),
    ("{\"one\": \"1\", \"two\": [2], \"three\": 3, \"four\": 4.6}",
     "{\"one\": \"\", \"two\": [], \"three\": 0, \"four\": 0}"),
    ("{\"colorsArray\":[{\"colorName\":\"red\",\"hexValue\":\"f00\"},{\"colorName\":\"green\",\"hexValue\":\"0f0\"},{\"colorName\":\"blue\",\"hexValue\":\"00f\"},{\"colorName\":\"cyan\",\"hexValue\":\"0ff\"},{\"colorName\":\"magenta\",\"hexValue\":\"f0f\"},{\"colorName\":\"yellow\",\"hexValue\":\"ff0\"},{\"colorName\":\"black\",\"hexValue\":\"000\"}]}",
     "{\"colorsArray\": []}"),
]
testFunction(testCases, buildCommand, 'buildCommand')
