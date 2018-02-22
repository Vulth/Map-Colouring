def selectNextNode(n, k, G, map_array, colour_array):
	 #Minimum Remaining Values
	 #Search the colour array to find the node with the fewest remaining colour choices

	 MRV = k + 1
	 for i in range(1, len(map_array)):
	 	if (MRV > len(colour_array[i])) & (len(colour_array[i]) > 1) & (map_array[i] == 0):
	 		MRV = len(colour_array[i])
	 
	 #Degree
	 #Degree is a tiebreaker when there are multiple nodes tied for fewest remaining values
	 #chooses the node with the most connections to other unassigned nodes
	 highest_degree_node = "null"
	 highest_degree = -1
	 print("the MRV is", MRV)
	 for i in range(1, n+1): #this for loop will iterate through the whole array, settling on the nodes with the fewest remaining values. It compares each node's adjacency list to find the node with the highest degree
	 	if (len(colour_array[i]) == MRV) & (map_array[i] == 0): 
	 		adjacent_node_list = G[i-1] #get the list of all nodes adjacent to the coloured node

	 		contender_degree = 0
	 		for j in range(1, len(adjacent_node_list)):
	 			if map_array[adjacent_node_list[j]] == 0:
	 				contender_degree = contender_degree + 1 # count the number of adjacent uncoloured nodes
	 		print("node[", i, "] has a degree of ", contender_degree)
	 		if contender_degree > highest_degree: # if the new node has more uncoloured adjacent nodes than the previous highest, then change the highest
	 			highest_degree = contender_degree
	 			highest_degree_node = i

	 print("the highest degree node is", highest_degree_node, "with a degree of ", highest_degree)
	 for i in range(len(colour_array)):
	 	print(colour_array[i])
	 return highest_degree_node

def leastConstrainingValue(n, k, G, map_array, colour_array, node):
	colour_order = []
	value_array = [-1]
	max_value = [-1]
	for i in range(1, len(colour_array[node])):
		value = 0
		current_colour = colour_array[node][i]
		adjacent_node_list = G[node-1]
		for j in range(1, len(adjacent_node_list)):
			adjacent_node = adjacent_node_list[j]
			if (current_colour in colour_array[adjacent_node]):
				value = value + len(colour_array[adjacent_node]) - 1
			else:
				value = value + len(colour_array[adjacent_node])

		print("when using colour", current_colour, "for node", node, "has a value of", value)
		value_array.append(value)
		max_value.append(value)

	max_value.sort()	

	while (len(max_value) > 1):
		for i in range(1, len(value_array)):
			if value_array[i] == max_value[len(max_value) - 1]:
				colour_order.append(colour_array[node][i])
				max_value.remove(max_value[len(max_value) - 1])

	return colour_order

def legalLayout(n, k, G, map_array, colour_array):
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

	return True

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
	print("the current map array is:", map_array)
	node = selectNextNode(n, k, G, map_array, colour_array)
	if node == "null":
		return []
	colour_choice_list = leastConstrainingValue(n, k, G, map_array, colour_array, node)
	for i in range (len(colour_choice_list)):
		current_colour = colour_choice_list[i]
		map_array[node] = current_colour
		colour_array[node].remove(current_colour)
		adjacent_node_list = G[node-1]
		altered_node_list = []
		for j in range(1, len(adjacent_node_list)):
			adjacent_node = adjacent_node_list[j]
			if current_colour in colour_array[adjacent_node]:
				colour_array[adjacent_node].remove(current_colour)
				altered_node_list.append(adjacent_node)

		if legalLayout(n, k ,G, map_array, colour_array):
			solution = backtracking(n, k, G, map_array, colour_array)
			if solution != []:
				return solution

		map_array[node] = 0
		colour_array[node].append(current_colour)
		for j in range(len(altered_node_list)):
			colour_array[altered_node_list[j]].append(current_colour)

	return []

def solve(n, k, G):
	map_array = [0 for i in range(0, n+1)] #map_array will map colours to the nodes on the map, map_array[1] will designate the colour of node 1 and so on
	colour_array = [[i for i in range(k + 1)] for j in range(n + 1)] #colour array holds the legal colours left for each node
	
	solution = backtracking(n, k, G, map_array, colour_array)
	return solution

G = [[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]] # a list of lists
n = 5 # number of vertices
k = 2 # number of colours
#solution = solve(n, k, G)
#print(solution)


G = [[1, 2, 3], [2, 1, 3, 4], [3, 1, 2, 4, 5, 6], [4, 2, 3, 5], [5, 3, 4, 6], [6, 3, 5]]
n = 6
k = 3
map_array = [0, 1, 2, 0, 0, 0, 0]
colour_array = [[], [0, 3], [0, 3], [0, 3], [0, 1, 3], [0, 1, 2, 3], [0, 1, 2 ,3]]
node = 4
#solution = solve(n, k, G)
#print(solution)

G = [[1, 2, 3, 4, 6, 7, 10], [2, 1, 3, 4, 5, 6], [3, 1, 2], [4, 1, 2], [5, 2, 6], [6, 1, 2, 5, 7, 8], [7, 1, 6, 8, 9, 10], [8, 6, 7, 9], [9, 7, 8, 10], [10, 1, 7, 9]]
n = 10
k = 3
solution = solve(n, k, G)
print(solution)
# print("solution is", solution)