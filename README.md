# Map-Colouring
## A program written in Python that will assign colours to a set of connected nodes such that no adjacent nodes will have the same colour

### Program Design:

The program starts by calling solve, which will allocate two arrays 
Map_array keeps track of each node and the colour it has been assigned.
Map_array[1] = 2 indicates that node 1 has been assigned the colour 2.
The 0th index is unused.
If a node has the value 0, that means it has not been assigned a colour yet.
Colour_array is a list of lists, where colour_array[1] is the list of colours that node 1 can be legally assigned.

After allocating these two lists, the recursive backtracking search function is called.

Backtracking will first check if the Map_array is completely filled. If it is, it will return Map Array as a valid solution to the nodes. If it is not completely filled, it will call selectNextNode to determine the best node to assign a colour to.

SelectNextNode uses the minimum remaining values and degree heuristics to determine which node is optimal for solving the node puzzle. If SelectNextNode returns a null, the current colour assignments are unviable. The program will go back a step and try the next legal colour. Once a node has been chosen by SelectNextNode, LeastConstrainingValue will be used to create a list of best to worst colour choices for the chosen node.

LeastConstrainingValue will return a list of the best to worst colour choices by adding together the remaining colour choices of each adjacent node if colour x is chosen. The colour that has the most adjacent colour choices remaining is the best choice. Once the list has been compiled, LeastConstrainingValue will return the list to Backtracking.

Backtracking will then start with the optimal colour choice, assign it to the node, remove that colour option from each of the adjacent nodes, and check if the current colour allocation is legal. If it is, it will then recursively call itself, passing along the current map_array and colour_array
If backtracking returns an empty list, that means that the current map_array will not lead to a legal map colouring. It resets the current node to an uncoloured state, returns the chosen colour to the list of legal colours for each adjacent node, and tries the next colour in the list from LeastConstrainingValue. If none of the colours in the list result in a legal layout, then Backtracking will return an empty list to its caller.

If every choice of colours results in an illegal layout, then the current map cannot be coloured with the given number of colours.
