# maze-python-project

# MAZE SOLVER PRPJECT BY NILESH YADAV


# Project description:

 A maze in the form of matrix will be given in the form of 1’s and 0’s, where 1 represents the open path and 0 represents the blocked path.

	And the goal is to find the path between the source to the destination in the maze (if the path exists) otherwise just return/print -1 indicating no path exists between the source and destination.

# Concepts used:
	Graphs
	Breadth-First-Search Algorithm
	Dijkstra’s Algorithm
	File Handling

# Algorithm for Solving the Problem:
	From the given matrix identify the positions, which has 1 and take them as vertices(nodes) of the graph
	Then, identify the positions(neighbours) which are immediate left, right, top and bottom, to a given node, if contains 1 .
	Whichever neighbour contains 1 for a given node, add that particular node as neighbour to the given node.
	Repeat the process until we obtain the entire undirected-unweighted graph.
	Now determine if the two nodes (i.e the source-node and the destination-node) connected.
	If the two nodes are connected, then determine the path between them (i.e identify the positions)
	Finally, print the matrix of the order (which is equal to the order of input) which contains 1 at the positions obtained from the above process and contains 0 at other positions.

# Execution:

# Input:
	This code can be run by commandline
    input command formmat is as below
        <filename> <inputfile name> <outputfile name> --s="source" --d="destination"
        e.g.
            maze.py input.file outputfile --s=0,0 --d=3,3


# Description of Code:

	Create a class, say Graph.

	Define init dunder method, which contains graph attribute which is used in creating dictionary of vertices/nodes as keys and the neighbours of each node in the form of list as values.
	Also create an attribute prev_vertex which is used in creating a dictionary, which contains nodes as keys and their previous vertex in the path as value

	Add_edge method is used to add nodes and their neighbours in the graph
	Of course this method is also used to update the edges and weights attributes

	if_path_exits method was defined and it uses Breadth-First-Search approach to find if two nodes are connected / if there is a path between two nodes.
	This method returns Boolean based on whether there is a path between two nodes.

	shortestpath method was defined to find the shortest distance between the given node and all other nodes

	This method is also used in identifying the path between two nodes (if they are connected) by constantly updating the prev_vertex attribute.

	This method returns the prev_vertex dictionary to source_to_destination method.

	source_to_destination method was defined to employ the above two methods and return the corresponding output
	If there is path between two given nodes i.e if the two nodes are connected then the source_to destination method returns the positions/set of vertices of the given path.
	Else returns -1 indicating the two given nodes are not connected.


# Output:
	Open a file, say output.txt, in write mode
	Define a nested list of order of the input matrix and initialize all the values as 0’s
	Equate the positions of matrix, corresponding to the positions of the output of source_to_destination method from class Graph ,to 1.
	Now write each element (line by line manner) in the output matrix(nested list) in the string format in the output.txt. 
	If the output from source_to_destination method from class Graph is -1 then write it in the string format in the output.txt
	Close the file output.txt

