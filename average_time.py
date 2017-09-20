# https://codefights.com/challenge/vRAkSzkpnqJGo4z6F/

from utils import benchmark, testFunction
from math import factorial

class Tree:
    def __init__(self, theMap):
        self.numberOfTowns = len(theMap) + 1
        self.possibleLeaves = None
        roads = {}
        self.numberOfChildren = {}
        for t0, t1, h in theMap:
            if t0 not in roads:
                roads[t0] = {}
                self.numberOfChildren[t0] = 0
            if t1 not in roads:
                roads[t1] = {}
                self.numberOfChildren[t1] = 0
            roads[t0][t1] = [t0, h]
            roads[t1][t0] = [t1, h]
        self.roads = roads

    def numberOfPaths(self, leaf):
        if len(self.roads[leaf]) != 1:
            raise ValueError("This is not a leaf")
        nc = self.numberOfChildren[leaf]
        nt = self.numberOfTowns
        return (nc + 1)*(nt-(nc + 1))

    def getPaths(self, town):
        paths = []
        for key, value in self.roads[town].items():
            paths.append((key, value[0], value[1]))
        return paths

    def __str__(self):
        result = ""
        for town in self.roads:
            result += "-"*20 + "town" + str(town) + "-"*20 + "\n"
            result += "children : " + str(self.numberOfChildren[town]) + "\n"
            for town1, town2, roadTime in self.getPaths(town):
                result += "(" + str(town1) + ", " + str(town2) + ")=" + str(roadTime) + "\n"
        return result

    def getParent(self, leaf):
        if len(self.roads[leaf]) > 1:
            raise ValueError("Can't get parent, not a leaf")
        if len(self.roads[leaf]) == 0: # It's the root
            return None
        return list(self.roads[leaf].keys())[0]

    def getLeaves(self):
        leaves = []
        if len(self.roads) == 2:
            return [list(self.roads.keys())[0]]

        if self.possibleLeaves is None:
            for town in self.roads:
                if len(self.roads[town]) == 1:
                    leaves.append(town)
        else:
            for town in self.possibleLeaves:
                if len(self.roads[town]) == 1:
                    leaves.append(town)
        return leaves

    def __len__(self):
        return len(self.roads)

    def removeLeaves(self, leaves):
        self.possibleLeaves = set()
        for leaf in leaves:
            parent = self.getParent(leaf)
            if parent is not None:
                del self.roads[parent][leaf]
                self.numberOfChildren[parent] += 1 + self.numberOfChildren[leaf]
                self.possibleLeaves.add(parent)
            del self.roads[leaf]

    def roadTime(self, leaf):
        paths = self.getPaths(leaf)
        if len(paths) > 1:
            raise ValueError("It is not a leaf")
        if len(paths) == 0:
            raise ValueError("It seems to be the town")
        return paths[0][2]

def averageTime(theMap):
    if len(theMap) == 0:
        return 0
    tree = Tree(theMap)
    towns = tree.numberOfTowns
    numberOfPath = towns * (towns - 1) // 2

    sumOfPath = 0
    while len(tree) > 1:
        leaves = tree.getLeaves()
        sumOfPath += sum(tree.roadTime(leaf)*tree.numberOfPaths(leaf) for leaf in leaves)
        tree.removeLeaves(leaves)

    return round(sumOfPath / numberOfPath, 6)

testCases = [
    ([[1,2,3],
      [2,3,4],
      [2,4,2]], 4.5),
    ([[1,2,2],
      [2,3,1],
      [3,5,7],
      [2,4,1],
      [1,6,9],
      [6,7,1]], 8.47619),
    ([[1,2,5],
      [2,3,1],
      [2,5,2],
      [3,4,1],
      [3,6,3]], 4.266667),
    ([], 0)
]

tree = Tree(testCases[2][0])

testFunction(testCases, averageTime, 'averageTime')
