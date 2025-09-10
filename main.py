from objects.graph import Graph

g = Graph(1, 4, 3, 5)
for node in g.vertices:
    print(node.nodeID, node.adjascentVertices)

g.setNodeInfo({1: {2:4, 3:2, 0:2, 4:3}, 0: {2:3, 4:3}})
for node in g.vertices:
    print(node.nodeID, node.adjascentVertices)
