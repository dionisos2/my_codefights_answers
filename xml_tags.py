# https://codefights.com/arcade/python-arcade/picturing-the-parsibilities/93XzHLkTAQXJYzdFd

from utils import benchmark, testFunction
from collections import OrderedDict
import xml.etree.ElementTree as ET

def depthIter(element):
  stack = []
  stack.append(iter(element))
  yield (element, 0)
  while stack:
    currentElement = next(stack[-1], None)
    if currentElement is None:
      stack.pop()
    else:
      yield (currentElement, len(stack))
      stack.append(iter(currentElement))



def xmlTags(xml):
  result = []
  tags = OrderedDict()
  root = ET.fromstring(xml)
  for element, depth in depthIter(root):
    if element.tag not in tags:
      tags[element.tag] = [depth, set(element.keys())]
    else :
      tags[element.tag][1] |= set(element.keys())

  for tag, value in tags.items():
    properties = ', '.join(sorted(value[1]))
    result.append('--'*value[0]+tag+'('+properties+')')
  return result


testCases = [
  ("<data><animal name=\"cat\"><genus>Felis</genus><family name=\"Felidae\" subfamily=\"Felinae\"/><similar name=\"tiger\" size=\"bigger\"/></animal><animal name=\"dog\"><family name=\"Canidae\" member=\"canid\"/><order>Carnivora</order><similar name=\"fox\" size=\"similar\"/></animal></data>",
   ["data()", "--animal(name)", "----genus()", "----family(member, name, subfamily)", "----similar(name, size)", "----order()"]),
  ("<products><product><TITLE> product #1 </TITLE><PRICE> 10.00 </PRICE></product><product><TITLE> product #2 </TITLE><PRICE> 20.00 </PRICE></product></products>",
   ["products()", "--product()", "----TITLE()", "----PRICE()"]),
  ("<here urlid=\"blah-blah\"><component type=\"Documents\" context=\"User\"><displayName>My Video</displayName><role role=\"Data\"><detects><detect><condition>Helper.hasObject</condition></detect></detects><rules><include filter=\"Helper.IgnoreIrrelevantLinks\"><objectSet><pattern type=\"File\"></pattern></objectSet></include></rules></role></component></here>",
   ["here(urlid)", "--component(context, type)", "----displayName()", "----role(role)", "------detects()", "--------detect()", "----------condition()", "------rules()", "--------include(filter)", "----------objectSet()", "------------pattern(type)"])
]

testFunction(testCases, xmlTags, 'xmlTags')
