#graphe representation
adj_list = {
    "A" : ["B"],
    "B" : ["D", "E"],
    "C" : ["F"],
    "D" : [],
    "E" : [],
    "F" : ["C"],
}


#initialization
color = {}
parent = {}
trav_time = {}
dfs_traversal_output = []

for node in adj_list.keys():
	color[node] = "W"
	parent[node] = None
	trav_time[node] = [-1, -1]#inf #inf
	
time = 0

def dfs_util(u):
	global time
	color[u] = "G"
	dfs_traversal_output.append(u)
	trav_time[u][0] = time
	time += 1
	
	for v in adj_list[u]:
		if color[v] == "W":
			parent[v] = u
			dfs_util(v)
	color[u] = "B"
	trav_time[u][1] = time
	time += 1
	
#dfs_util("A")
for u in adj_list.keys():
	if color[u] == "W":
		dfs_util(u)

print(dfs_traversal_output)
print(trav_time)
print(parent)
		
			
			