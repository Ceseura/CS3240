__author__ = 'all5dh'

class Graph:
	""" Uses the built-in python dict to hold data for a Graph. """
	def __init__(self, input = {}):
		""" Create a graph with optional dictionary as input """
		# TODO: Assumes input is a valid graph
		self.data = input

	def get_adjlist(self, node):
		""" Return the list of nodes adjacent to 'node', or False if 'node' is not in the graph. """
		# TODO: return None instead of false?
		if node not in self:
			return None
		else:
			return self.data[node]

	def is_adjacent(self, node1, node2):
		""" Return True if 'node1' and 'node2' are adjacent, otherwise False. """
		return node1 in self and node2 in self.data[node1]

	def num_nodes(self):
		""" Returns the number of nodes in the graph. """
		return self.__len__()

	def __str__(self):
		""" Returns a string describing the graph. """
		return "Graph with {}".format(self.data)

	def __iter__(self):
		""" Returns an iterator over the nodes in the graph. """
		return self.data.__iter__()

	def __contains__(self, node):
		""" Returns True if 'node' is in the graph, otherwise False. """
		return node in self.data

	def __len__(self): 
		""" Returns the number of nodes in the graph. """
		return len(self.data)

	def add_node(self, node):
		""" Tries to adds a new node to the graph. Returns False if 'node' is already in the graph, otherwise True. """
		if node in self:
			return False
		else:
			self.data[node] = []
			return True


	def link_nodes(self, node1, node2):
		""" Tries to link two nodes in the graph. Returns False if the two nodes are already adjacent, or if either node is not in the graph, or if the two nodes are the same, otherwise True. """
		if node1 not in self or node2 not in self or node1 == node2 or node2 in self.data[node1]:
			return False
		else:
			self.data[node1].append(node2)
			self.data[node2].append(node1)
			return True

	def unlink_nodes(self, node1, node2):
		""" Tries to unlink two nodes in the graph. Returns False if the nodes are not initially adjacent, or if either node is not in the graph, otherwise True. """
		if node1 not in self or node2 not in self or node1 == node2 or node2 not in self.data[node1]:
			return False
		else:
			self.data[node1].remove(node2)
			self.data[node2].remove(node1)
			return True

	def del_node(self, node):
		""" Tries to remove the node and all edges connected to the node. Returns False if 'node' is not in the graph, otherwise True. """
		if node not in self:
			return False
		else:
			del self.data[node]
			for remainingNode in self:
				if node in self.data[remainingNode]:
					self.data[remainingNode].remove(node)
			return True