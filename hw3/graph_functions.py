__author__ = "all5dh"
from graph import Graph

def is_complete(grph):
	""" Return True if grph is a complete graph (every node is adjacent to every other node). Raises TypeError if grph is not a Graph object."""
	if not isinstance(grph, Graph):
		raise TypeError

	if grph.num_nodes() < 2:
		return True

	for node in grph:
		if not len(grph.get_adjlist(node)) == grph.num_nodes() - 1:
			return False

	return True

def nodes_by_degree(grph):
	""" Return a sorted (decending by degree) list of (node_name, degree) tuples. Raises TypeError if grph is not a Graph object. """
	if not isinstance(grph, Graph):
		raise TypeError

	out = []

	for node in grph:
		out.append((node, len(grph.get_adjlist(node))))

	return sorted(out, key=lambda x: x[1], reverse=True)

