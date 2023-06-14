def hamilton(graph, chemin=[]):
	if not chemin:
		chemin.append(0)
	if len(chemin) == len(graph) and chemin[-1] == (len(graph) - 1):
		return chemin
	for voisin in range(1, len(graph)):
		if graph[chemin[-1]][voisin] == 1 and voisin not in chemin:
			cycle = hamilton(graph, chemin + [voisin])
			if cycle:
				return cycle
	return []
	

def afficherSolution(chemin):
	if chemin:
		print("Le chemin hamiltonien pour ce graphe est :")
		for sommet in chemin:
			if not sommet:
				print(sommet, end="")
		#print(chemin[0])
			else:
				print(f"---{sommet}", end="")
	else:
		print("Pas de chemin hamiltonien pour ce graphe")
		
if __name__ == "__main__":
	g1 = [
		[0, 1, 0, 1, 0],
		[1, 0, 1, 1, 1],
		[0, 1, 0, 0, 1],
		[1, 1, 0, 0, 1],
		[0, 1, 1, 1, 0]
	]
	
	afficherSolution(hamilton(g1))
	g2 = [
		[0, 1, 1, 1, 1, 1, 0, 0 ,0 ,0, 0],
		[1, 0, 1, 1, 0, 0, 1, 1 ,0 ,0, 0],
		[1, 1, 0, 0, 0, 1, 1, 0 ,0 ,0, 0],
		[1, 0, 0, 0, 1, 1, 0, 0 ,0 ,1, 0],
		[1, 0, 0, 1, 0, 0, 0, 0 ,0 ,1, 1],
		[1, 0, 1, 1, 0, 0, 0, 0 ,1 ,1, 1],
		[0, 1, 1, 0, 0, 0, 0, 1 ,1 ,0, 0],
		[0, 1, 0, 0, 0, 0, 1, 0 ,1 ,0, 1],
		[0, 0, 0, 0, 0, 1, 1, 1 ,0 ,0, 1],
		[0, 0, 0, 1, 1, 1, 0, 0 ,0 ,0, 1],
		[0, 0, 0, 0, 1, 1, 0, 1 ,1 ,1, 0]
	]
	print("")
	afficherSolution(hamilton(g2))