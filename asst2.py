def selectNextNode(n, k, G, map_array, colour_array):
	 #Minimum Remaining Values
	 #Search the colour array to find the node with the fewest remaining colour choices

	 MRV = k + 1
	 for i in range(1, len(map_array)):
	 	if MRV > len(colour_array[i]):
	 		MRV = len(colour_array[i])

	 #Degree
	 #Degree is a tiebreaker when there are multiple nodes tied for fewest remaining values
	 #chooses the node with the most connections to other unassigned nodes
	 highest_degree_node = -1
	 highest_degree = -1

	 for i in range(1, n+1): #this for loop will iterate through the whole array, settling on the nodes with the fewest remaining values. It compares each node's adjacency list to find the node with the highest degree
	 	if len(colour_array[i]) == MRV: 

	 		adjacent_node_list = G[i-1] #get the list of all nodes adjacent to the coloured node
	 		contender_degree = 0
	 		for j in range(1, len(adjacent_node_list)):
	 			if map_array[adjacent_node_list[j]] == 0:
	 				contender_degree = contender_degree + 1 # count the number of adjacent uncoloured nodes
	 		if contender_degree > highest_degree: # if the new node has more uncoloured adjacent nodes than the previous highest, then change the highest
	 			highest_degree = contender_degree
	 			highest_degree_node = i

	 return highest_degree_node

def legalLayout(n, k, g, map_array, colour_array):
	#check if any adjacent nodes have the same colour. If two adjacent nodes do have the same colour, make sure they are uncoloured
	for i in range(0, len(G)):
		current_list = G[i]
		current_node = current_list[0]
		for j in range(1, len(current_list)):
			if (map_array[current_node] == map_array[current_list[j]]):
				if map_array[current_node] != 0:
					return False

	#check if an uncoloured node has no remaining legal colour values
	for i in range(1, n+1):
		if (map_array[i] == 0 & len(colour_array[i]) == 1):
			return False

def completeness(n, k, G, map_array):
	#check if the whole map has been coloured yet
	for i in range(1, n + 1):
		if map_array[i] == 0:
			return False
	return True

def backtracking(n, k, G, map_array, colour_array):
	#if map_array is filled out and legal, then return this assignment of colours
	complete = completeness(n, k, G, map_array)
	if complete == True:
		return map_array

	map_array = [0, 1, 2, 0, 0, 0]
	colour_array = [[], [0, 3], [0, 3], [0, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
	node = selectNextNode(n, k, G, map_array, colour_array)
	print("The next node is", node)
		

def solve(n, k, G):
	map_array = [0 for i in range(0, n+1)] #map_array will map colours to the nodes on the map, map_array[1] will designate the colour of node 1 and so on
	colour_array = [[i for i in range(k + 1)] for j in range(n + 1)] #colour array holds the legal colours left for each node
	
	solution = backtracking(n, k, G, map_array, colour_array)
	return solution

G = [[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]] # a list of lists
n = 5 # number of vertices
k = 3 # number of colours
solution = solve(n, k, G)


# print("solution is", solution)