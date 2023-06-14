class EnsembleDisjoint:
	parent = {}
	def __init__(self, N):
		for i in range(N):
			self.parent[i] = i
			
	def get_parent(self, k):
		if self.parent[k] == k:
			return k
		return self.get_parent(self.parent[k])
		
	def union(self, a, b):
		#x = self.get_parent(a)
		#y = self.get_parent(b)
		
		self.parent[b] = a

##_Algo_KRUSKAL_
def kruskal(arcs, nb_sommets):
	ed = EnsembleDisjoint(nb_sommets)
	arbre_minimum = []
	index = 0
	while len(arbre_minimum) != (nb_sommets - 1):
		(src, dest, poids) = arcs[index]
		index += 1
		
		x = ed.get_parent(src)
		y = ed.get_parent(dest)
		
		if x != y:
			arbre_minimum.append((src, dest, poids))
			ed.union(x, y)
			
	return arbre_minimum

##__main()__			
if __name__ == "__main__":
	
	arcs = [ (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5), (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)]
	
	arcs.sort(key=lambda x: x[2])
	nb_sommets = 7
	
	print("The minimum spaning tree is : \n", kruskal(arcs, nb_sommets))