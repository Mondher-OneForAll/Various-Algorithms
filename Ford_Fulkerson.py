from math import inf

class Graph:
	def __init__(self, graph):
		self.graph = graph
		self.ROW = len(graph)
		
	def searching_algo_bfs(self, s, t, parent):
		visited = [False] * self.ROW
		queue = []
		queue.append(s)
		visited[s] = True
		
		while queue:
			u = queue.pop()
			
			for i , val in enumerate(self.graph[u]):
				if visited[i] == False and val > 0:
					queue.append(i)
					visisted[i] = True
					parent[i] = u
					
		return True if visited[t] else False
	
	def ford_fulkerson(self, source, sink):
		parent = [-1] * self.ROW
		max_flow = 0
		
		while searching_algo_bfs(source, sink, parent):
			path_flow = inf
			t = sink
			
			while(t != source):
			    path_flow = min(path_flow, self.graph[parent[t]][t])
				t = parent[t]
				
			#Adding path flows
			max_flow += path_flow
			
			#Updating the residual values of edges
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]
				
		return max_flow
				
				
if __name__ == "main":
	
	graph = [
		[0, 8, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 7, 2],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 7, 4, 0, 0],
        [0, 0, 0, 0, 0, 0]
	]

	g = Graph(graph)
	parent = [-1] * self.ROW
	print(parent)	
	
	source = 0
	sink = 5
	
	print("Max flow :", g.ford_fulkerson(source, sink))