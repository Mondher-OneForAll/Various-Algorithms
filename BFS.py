from queue import Queue

adj_list = {
    "A" : ["B", "D"],
    "B" : ["A", "C"],
    "C" : ["B"],
    "D" : ["A", "E", "F"],
    "E" : ["D", "F", "G"],
    "F" : ["D", "E", "H"],
    "G" : ["E", "H"],
    "H" : ["F", "G"]
}

#initialization:
visited = {}
parent = {}
level = {}
bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys():
	visited[node] = False
	parent[node] = None
	level[node] = -1#inf

#BFS
s = "A"
level[s] = 0
visited[s] = True
queue.put(s)

while not queue.empty():
	u = queue.get()
	bfs_traversal_output.append(u)
	
	for v in adj_list[u]:
		if not visited[v]:
			visited[v] = True
			parent[v] = u
			level[v] = level[u] + 1
			queue.put(v)
print("BFS traversal output is : ")
print(bfs_traversal_output)

#Shortest distance from all node to source node
v = "G"
print(f"Distance from {v} to source node is : {level[v]}")
print("Distance from all nodes to source node :")
print(level)

#Shortest path from any node to source node
v = "G"
path = []

while v is not None:
	path.append(v)
	v = parent[v]

path.reverse()
print(f"Path from A to source node is : \n{path}")
