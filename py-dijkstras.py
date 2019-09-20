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
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    costs = costs[node]
    neighbors = graph[node]
    for n in neighbors
