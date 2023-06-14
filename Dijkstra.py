from math import inf
def dijkstra(village, source="white"):
	
	#Assertion:
	assert  all(village[u][v] >= 0 for u in village.keys() for v in village[u].keys())
	
	#initialization:
	visited = {node:False for node in village.keys()}
	parent = {node:None for node in village.keys()}
	distance = {node:inf for node in village.keys()}
	
	distance[source] = 0
	a_traiter = [(source, 0)]
	
	#__Algo__:
	while a_traiter:
		v, dist = a_traiter.pop()
		if not visited[v]:
			visited[v] = True
			for u in village[v].keys():
				if dist + village[v][u] < distance[u]:
					distance[u] = dist + village[v][u]
					parent[u] = v
					a_traiter.append((u, distance[u]))
			
		a_traiter.sort(reverse=True)
		
	return distance, parent
			
		






if __name__ == "__main__":
	
	village = {
		"white" : {"blue" : 3, "yellow" : 12},
		"blue" : {"white" : 1, "red" : 5, "gris" : 2},
		"gris" : {"blue" : 2, "red" : 1},
		"red" : {"gris" : 1, "yellow" : 4},
		"yellow" : {"red" : 4, "white" : 12}
	}
	
	distance, parent = dijkstra(village)
	
	print(distance)
	print(parent)