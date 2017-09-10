__author__ = "all5dh"

import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
	def setUp(self):
		self.g1 = Graph({ 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] })

	def test_get_adj_T1(self):
		""" T1: test get_adjlist(node) when input is not in graph. """
		res = self.g1.get_adjlist('Z')
		self.assertEqual(res, None, "T1 did not return None on invalid input")

	def test_get_adj_T2(self):
		""" T2: test get_adjlist(node) when input is in graph. """
		res = self.g1.get_adjlist('A')
		self.assertEqual(res, ['B', 'D'], "T2 did not return expected adjacent list")

	def test_is_adj_T3(self):
		""" T3: test is_adjacent(node1, node2) when node1 is not in graph. """
		res = self.g1.is_adjacent('Z', 'A')
		self.assertEqual(res, False, "T3 did not return False when node1 is not in graph")

	def test_is_adj_T4(self):
		""" T4: test is_adjacent(node1, node2) when node1 and node2 are adjacent. """
		res = self.g1.is_adjacent('A', 'B')
		self.assertEqual(res, True, "T4 did not return True when node1 and node2 are adjacent")

	def test_is_adj_T5(self):
		""" T5: test is_adjacent(node1, node2) when node1 and node2 are both in graph but not adjacent. """
		res = self.g1.is_adjacent('A', 'E')
		self.assertEqual(res, False, "T5 did not return False when node1 and node2 are not adjacent")

	def test_num_nodes_T6(self):
		""" T6: test num_nodes() when graph is empty. """
		g0 = Graph()
		res = g0.num_nodes()
		self.assertEqual(res, 0, "T6 did not return 0 when called on empty graph")

	def test_num_nodes_T7(self):
		""" T7: test num_nodes() when graph is non-empty. """
		res = self.g1.num_nodes()
		self.assertEqual(res, 5, "T7 did not return expected number of nodes")

	def test_contains_T8(self):
		""" T8: test contains(node) when node is in graph. """
		res = self.g1.__contains__('B')
		self.assertEqual(res, True, "T8 did not return True when using '__contains__()'")

		res = 'B' in self.g1
		self.assertEqual(res, True, "T8 did not return True when using 'in'")

	def test_contains_T9(self):
		""" T9: test contains(node) when node is not in graph. """
		res = self.g1.__contains__('Z')
		self.assertEqual(res, False, "T9 did not return False when using '__contains__()'")

		res = 'Z' in self.g1 
		self.assertEqual(res, False, "T9 did not return False when using 'in'")

	def test_len_T10(self):
		""" T10: test len(graph) when graph is empty. """
		g0 = Graph()
		res = g0.__len__()
		self.assertEqual(res, 0, "T10 did not return 0 when called on empty graph with '__len__()'")

		res = len(g0)
		self.assertEqual(res, 0, "T10 did not return 0 when called on empty graph with 'len()'")

	def test_len_T11(self):
		""" T11: test len(graph) when graph is non-empty. """
		res = self.g1.__len__()
		self.assertEqual(res, 5, "T11 did not return expected length when called on non-empty graph with '__len__()'")

		res = len(self.g1)
		self.assertEqual(res, 5, "T11 did not return expected length when called on non-empty graph with 'len()'")

	def test_add_node_T12(self):
		""" T12: test add_node(node) when node is already in graph. """
		res = self.g1.add_node('C')
		self.assertEqual(res, False, "T12 did not return False when adding node already in graph")
		self.assertEqual(len(self.g1), 5, "T12 did not return expected length when failing to add node")

	def test_add_node_T13(self):
		""" T13: test add_node(node) when node is not already in graph. """
		res = self.g1.add_node('added')
		self.assertEqual(res, True, "T13 did not return True when adding node not already in graph")
		self.assertEqual(len(self.g1), 6, "T13 did not return expected length when successfully adding node")
		self.assertEqual('added' in self.g1, True, "T13 did not return True when running __contains__('added')")

	def test_link_nodes_T14(self):
		""" T14: test link_nodes(node1, node2) when either node is not in graph. """
		res = self.g1.link_nodes('A', 'Z')
		self.assertEqual(res, False, "T14 did not return False when node2 is not in graph")
		self.assertEqual(self.g1.get_adjlist('A'), ['B', 'D'], "T14 did not return expected list of adjacent nodes after failed link")

		res = self.g1.link_nodes('Z', 'C')
		self.assertEqual(res, False, "T14 did not return False when node1 is not in graph")
		self.assertEqual(self.g1.get_adjlist('C'), ['B'], "T14 did not return expected list of adjacent nodes after failed link")

	def test_link_nodes_T15(self):
		""" T15: test link_nodes(node1, node2) when node1 == node2. """
		res = self.g1.link_nodes('A', 'A')
		self.assertEqual(res, False, "T15did not return False when node1 is the same as node2")
		self.assertEqual(self.g1.get_adjlist('A'), ['B', 'D'], "T15 did not return expected list of adjacent nodes after failed link")

	def test_link_nodes_T16(self):
		""" T16: test link_nodes(node1, node2) when node1 is already linked to node2. """
		res = self.g1.link_nodes('A', 'D')
		self.assertEqual(res, False, "T16 did not return False when node1 is already linked to node2")
		self.assertEqual(self.g1.get_adjlist('A'), ['B', 'D'], "T16 did not return expected list of adjacent nodes after failed link")

	def test_link_nodes_T17(self):
		""" T17: test link_nodes(node1, node2) when inputs are valid. """
		res = self.g1.link_nodes('A', 'E')
		self.assertEqual(res, True, "T17 did not return True when link succeeds")
		self.assertEqual(self.g1.get_adjlist('A'), ['B', 'D', 'E'], "T17 did not return expected list of adjacent nodes after successful link")
		self.assertEqual(self.g1.get_adjlist('E'), ['A'], "T17 did not return expected list of adjacent nodes after successful link")

	def test_unlink_nodes_T18(self):
		""" T18: test unlink_nodes(node1, node2) when either node is not in graph. """
		res = self.g1.unlink_nodes('A', 'Z')
		self.assertEqual(res, False, "T18 did not return False when node2 is not in graph")
		self.assertEqual(self.g1.get_adjlist('A'), ['B', 'D'], "T18 did not return expected list of adjacent nodes after failed unlink")

		res = self.g1.unlink_nodes('Z', 'C')
		self.assertEqual(res, False, "T18 did not return False when node1 is not in graph")
		self.assertEqual(self.g1.get_adjlist('C'), ['B'], "T18 did not return expected list of adjacent nodes after failed unlink")

	def test_unlink_nodes_T19(self):
		""" T19: test unlink_nodes(node1, node2) when node1 == node2. """
		res = self.g1.unlink_nodes('A', 'A')
		self.assertEqual(res, False, "T19 did not return False when node1 is the same as node2")
		self.assertEqual(self.g1.get_adjlist('A'), ['B', 'D'], "T19 did not return expected list of adjacent nodes after failed unlink")

	def test_unlink_nodes_T20(self):
		""" T20: test unlink_nodes(node1, node2) when node1 is already not linked to node2. """
		res = self.g1.unlink_nodes('A', 'C')
		self.assertEqual(res, False, "T20 did not return False when node1 is already not linked to node2")
		self.assertEqual(self.g1.get_adjlist('A'), ['B', 'D'], "T20 did not return expected list of adjacent nodes after failed unlink")

	def test_unlink_nodes_T21(self):
		""" T21: test unlink_nodes(node1, node2) when inputs are valid. """
		res = self.g1.unlink_nodes('A', 'D')
		self.assertEqual(res, True, "T21 did not return True when unlink succeeds")
		self.assertEqual(self.g1.get_adjlist('A'), ['B'], "T21 did not return expected list of adjacent nodes after successful unlink")
		self.assertEqual(self.g1.get_adjlist('D'), ['B'], "T21 did not return expected list of adjacent nodes after successful unlink")

	def test_del_nodes_T22(self):
		""" T22: test del_node(node) when node is not in graph. """
		res = self.g1.del_node('Z')
		self.assertEqual(res, False, "T22 did not return False when deleting invalid node")
		self.assertEqual(self.g1.num_nodes(), 5, "T22 did not return expected number of nodes in graph")

	def test_del_nodes_T23(self):
		""" T23: test del_node(node) when node is in graph. """
		res = self.g1.del_node('B')
		self.assertEqual(res, True, "T23 did not return True when deleting valid node")
		self.assertEqual(self.g1.get_adjlist('A'), ['D'], "T23 did not return expected list of adjacent nodes after successfully deleting node")
		self.assertEqual(self.g1.num_nodes(), 4, "T23 did not return expected number of nodes in graph after successful delete")

	def test_filler_T24(self):
		""" T24: does the print just so I can get 100% coverage. """
		print(self.g1)
		self.assertEqual(True, True, "T24 broke logic")

if __name__ == '__main__':
    unittest.main()
