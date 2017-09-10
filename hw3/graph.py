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

if __name__ == "__main__":
	g = Graph( {'A' : ['B'], 'B' : ['A', 'C'], 'C' : ['B']} )
	print("__str__(): \n{}\n".format(g))

	print("get_adjlist():")
	print(g.get_adjlist('Z'))
	print(g.get_adjlist('B'))
	print("\n")
	print("is_adjacent():")
	print(g.is_adjacent('A', 'B'))
	print(g.is_adjacent('A', 'C'))
	print(g.is_adjacent('A', 'Z'))
	print(g.is_adjacent('Z', 'X'))
	print("\n")
	print("num_nodes():")
	print(g.num_nodes())
	print("\n")
	print("__contains__():")
	print('A' in g)
	print('Z' in g)
	print("\n")
	print("__iter__():")
	for node in g:
		print(node)
	print("\n")
	print("add_node():")
	print(g.add_node('D'))
	print(g.add_node('B'))
	print(g)
	print(g.num_nodes())
	print(g.get_adjlist('D'))
	print("\n")
	print("link_nodes():")
	print(g.link_nodes('Z', 'A'))
	print(g.link_nodes('B', 'Z'))
	print(g.link_nodes('Z', 'X'))
	print(g.link_nodes('D', 'A'))
	print(g.link_nodes('A', 'B'))
	print(g.link_nodes('A', 'A'))
	print(g)
	print(g.is_adjacent('A', 'D'))
	print("\n")
	print("unlink_nodes():")
	print(g.unlink_nodes('Z', 'A'))
	print(g.unlink_nodes('B', 'Z'))
	print(g.unlink_nodes('Z', 'X'))
	print(g.unlink_nodes('A', 'A'))
	print(g.unlink_nodes('A', 'C'))
	print(g.unlink_nodes('A', 'B'))
	print(g)
	print(g.is_adjacent('B', 'A'))
	print("\n")
	print("del_node():")
	print(g.del_node('Z'))
	print(g.del_node('A'))
	print(g)
