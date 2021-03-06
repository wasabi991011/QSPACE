from random import randint #problem?
import math

def perturb(added, i, j):
	#if we remove an edge, a random edge must be generated (vice versa)
	#this preserves avg valency
	#I add (ie remove from "needs to be removed" list) first
	#(so I don't add back the one I wanted to remove by chance)
	r = randint(0, len(added)-1)
	added.remove(r)
	#i, j specifies an edge to remove,
	#ie an edge that would need to be added to make the graph complete, so
	added.insert(0, [i,j])

	#get an adjmat from this "added" list
	#really added is a list of edges to add to make a comlpete graph
	#so starting at a complete graph and removing accoring to added gets the adjmat	

	#so if we use this perturbed added on a complete graph, using the same loop
	#as for the lattice, we get a perturbed graph
	return added

def getOldDist(adjmat, latmat): #DON'T COPY PASTE THIS
	#latmat is the adjmat of a perfect triangular lattice of equal size to adjmat
	n = len(adjmat)	
	for i in range(n):
		for j in range(i, n):
			if adjmat[i][j] == 1 and latmat[i][j] == 0: #new edge!
				#we explore top triangle, so i < j
				#vertex 1 is #i, 2 is #j
				#lattice should be a square lattice (before perturbation
				row_len = int(n**(1/2)) #in vertices
				col1 = i%row_len
				row1 = (i - col1)/row_len
				col2 = j%row_len
				row2 = (j - col2)/row_len
				
				col = abs(col2 - col1)
				row = abs(row2 - row1)
				if not col == 0 and not row == 0:
					row -= 1
	return int(col), int(row)

d1, d2 = getOldDist(perMatrix, latMatrix)
print(d1, d2)


