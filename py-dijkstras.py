# dijkstras algorithm
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

print(graph["start"].keys())

graph["a"] = {}
graph["a"]["b"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")
cost = {}
cost["a"] = 6
cost["b"] = 2
cost["fin"] = infinity

parents = {}
