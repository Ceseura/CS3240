__author__ = "all5dh"

import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
	def setUp(self):
		self.g1 = Graph({ 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] })

	def test_get_adj1(self):
		""" 1: test get_adjlist(node) when input is not in graph. """
		res = self.g1.get_adjlist('Z')
		self.assertEqual(res, None, "did not return None on invalid input")

	def test_get_adj2(self):
		""" 2: test get_adjlist(node) when input is in graph. """
		res = self.g1.get_adjlist('A')
		self.assertEqual(res, ['B', 'D'], "did not return expected adjacent list")

	def test_is_adj1(self):
		""" 3: test is_adjacent(node1, node2) when node1 is not in graph. """
		res = self.g1.is_adjacent('Z', 'A')
		self.assertEqual(res, False, "did not return False when node1 is not in graph")

	def test_is_adj2(self):
		""" 4: test is_adjacent(node1, node2) when node1 and node2 are adjacent. """
		res = self.g1.is_adjacent('A', 'B')
		self.assertEqual(res, True, "did not return True when node1 and node2 are adjacent")

	def test_is_adj3(self):
		""" 5: test is_adjacent(node1, node2) when node1 and node2 are both in graph but not adjacent. """
		res = self.g1.is_adjacent('A', 'E')
		self.assertEqual(res, False, "did not return False when node1 and node2 are not adjacent")

	def test_num_nodes1(self):
		""" 6: test num_nodes() when graph is empty. """
		g0 = Graph()
		res = g0.num_nodes()
		self.assertEquals(res, 0, "did not return 0 when called on empty graph")

	def test_num_nodes2(self):
		""" 7: test num_nodes() when graph is non-empty. """
		res = self.g1.num_nodes()
		self.assertEquals(res, 5, "did not return expected number of nodes")

	def test_contains1(self):
		""" 8: test contains(node) when node is in graph. """
		res = self.g1.__contains__('B')
		self.assertEquals(res, True, "did not return True when using '__contains__()'")

		res = 'B' in self.g1
		self.assertEquals(res, True, "did not return True when using 'in'")

	def test_contains2(self):
		""" 9: test contains(node) when node is not in graph. """
		res = self.g1.__contains__('Z')
		self.assertEquals(res, False, "did not return False when using '__contains__()'")

		res = 'Z' in self.g1 
		self.assertEquals(res, False, "did not return False when using 'in'")

	def test_len1(self):
		""" 10: test len(graph) when graph is empty. """
		g0 = Graph()
		res = g0.__len__()
		self.assertEquals(res, 0, "did not return 0 when called on empty graph with '__len__()'")

		res = len(g0)
		self.assertEquals(res, 0, "did not return 0 when called on empty graph with 'len()'")

	def test_len2(self):
		""" 11: test len(graph) when graph is non-empty. """
		res = self.g1.__len__()
		self.assertEquals(res, 5, "did not return expected length when called on non-empty graph with '__len__()'")

		res = len(self.g1)
		self.assertEquals(res, 5, "did not return expected length when called on non-empty graph with 'len()'")

	def test_add_node1(self):
		""" 12: test add_node(node) when node is already in graph. """
		res = self.g1.add_node('C')
		self.assertEquals(res, False, "did not return False when adding node already in graph")
		self.assertEquals(len(self.g1), 5, "did not return expected length when failing to add node")

	def test_add_node2(self):
		""" 13: test add_node(node) when node is not already in graph. """
		res = self.g1.add_node('added')
		self.assertEquals(res, True, "did not return True when adding node not already in graph")
		self.assertEquals(len(self.g1), 6, "did not return expected length when successfully adding node")
		self.assertEquals('added' in self.g1, True, "did not return True when running __contains__('added')")

	def test_link_nodes1(self):
		""" 14: test link_nodes(node1, node2) when either node is not in graph. """
		res = self.g1.link_nodes('A', 'Z')
		self.assertEquals(res, False, "did not return False when node2 is not in graph")
		self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'], "did not return expected list of adjacent nodes after failed link")

		res = self.g1.link_nodes('Z', 'C')
		self.assertEquals(res, False, "did not return False when node1 is not in graph")
		self.assertEquals(self.g1.get_adjlist('C'), ['B'], "did not return expected list of adjacent nodes after failed link")

	def test_link_nodes2(self):
		""" 15: test link_nodes(node1, node2) when node1 == node2. """
		res = self.g1.link_nodes('A', 'A')
		self.assertEquals(res, False, "did not return False when node1 is the same as node2")
		self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'], "did not return expected list of adjacent nodes after failed link")

	def test_link_nodes3(self):
		""" 16: test link_nodes(node1, node2) when node1 is already linked to node2. """
		res = self.g1.link_nodes('A', 'D')
		self.assertEquals(res, False, "did not return False when node1 is already linked to node2")
		self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'], "did not return expected list of adjacent nodes after failed link")

	def test_link_nodes4(self):
		""" 17: test link_nodes(node1, node2) when inputs are valid. """
		res = self.g1.link_nodes('A', 'E')
		self.assertEquals(res, True, "did not return True when link succeeds")
		self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D', 'E'], "did not return expected list of adjacent nodes after successful link")
		self.assertEquals(self.g1.get_adjlist('E'), ['A'], "did not return expected list of adjacent nodes after successful link")

	def test_unlink_nodes1(self):
		""" 18: test unlink_nodes(node1, node2) when either node is not in graph. """
		res = self.g1.unlink_nodes('A', 'Z')
		self.assertEquals(res, False, "did not return False when node2 is not in graph")
		self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'], "did not return expected list of adjacent nodes after failed unlink")

		res = self.g1.unlink_nodes('Z', 'C')
		self.assertEquals(res, False, "did not return False when node1 is not in graph")
		self.assertEquals(self.g1.get_adjlist('C'), ['B'], "did not return expected list of adjacent nodes after failed unlink")

	def test_unlink_nodes2(self):
		""" 19: test unlink_nodes(node1, node2) when node1 == node2. """
		res = self.g1.unlink_nodes('A', 'A')
		self.assertEquals(res, False, "did not return False when node1 is the same as node2")
		self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'], "did not return expected list of adjacent nodes after failed unlink")

	def test_unlink_nodes3(self):
		""" 20: test unlink_nodes(node1, node2) when node1 is already not linked to node2. """
		res = self.g1.unlink_nodes('A', 'C')
		self.assertEquals(res, False, "did not return False when node1 is already not linked to node2")
		self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'], "did not return expected list of adjacent nodes after failed unlink")

	def test_unlink_nodes4(self):
		""" 21: test unlink_nodes(node1, node2) when inputs are valid. """
		res = self.g1.unlink_nodes('A', 'D')
		self.assertEquals(res, True, "did not return True when unlink succeeds")
		self.assertEquals(self.g1.get_adjlist('A'), ['B'], "did not return expected list of adjacent nodes after successful unlink")
		self.assertEquals(self.g1.get_adjlist('D'), ['B'], "did not return expected list of adjacent nodes after successful unlink")

	# TODO: tests for del_node(node)
if __name__ == '__main__':
    unittest.main()
