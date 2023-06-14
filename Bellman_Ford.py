from math import inf
def bellman_ford(graph, origine):
	
	distance = [inf] * len(graph)
	distance[origine] = 0
	
	#__Algo__ :
	for _ in range(len(graph) - 1):
		for u in range(len(graph)):
			for v in range(len(graph)):
				if distance[u] + graph[u][v] < distance[v]:
					distance[v] = distance[u] + graph[u][v]
	
	#Recherche de cycle negatif : 
	for u in range(len(graph)):
		for v in range(len(graph)):
			if distance[u] + graph[u][v] < distance[v]:
				print("Le grapbe contient un cycle negatif !!")
				return
				
	return distance
	
if __name__ == "__main__":
	
	graph = [
		[0, -1, 4, inf, inf],
		[inf, 0, 3, 2, 2],
		[inf, inf, 0, inf, inf],
		[inf, 1, 5, 0, inf],
		[inf, inf, inf, -3, 0],	
	]
	
distance = bellman_ford(graph, 0)

for i in range(len(distance)):
	print(f" 0 -----> {i} : {distance[i]}")
				