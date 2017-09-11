__author__ = "all5dh"

import unittest
from graph import Graph
import graph_functions

class TestGraphFunctions(unittest.TestCase):
	def setUp(self):
		self.g0 = Graph()
		self.g1 = Graph({ 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] })
		self.g2 = Graph({ 'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B'] })
		self.g3 = Graph({'A':[]})
		self.not_a_graph = []

	def test_is_complete_False(self):
		res = graph_functions.is_complete(self.g1)
		self.assertEqual(res, False, "Expected False")

	def test_is_complete_True(self):
		res = graph_functions.is_complete(self.g2)
		self.assertEqual(res, True, "Expected True")

	def test_is_complete_Invalid(self):
		caught = False
		try:
			res = graph_functions.is_complete(self.not_a_graph)
		except TypeError:
			caught = True
		self.assertEqual(caught, True, "Expected True")

	def test_is_complete_Empty(self):
		res = graph_functions.is_complete(self.g0)
		self.assertEqual(res, True, "Expected True for empty")

	def test_is_complete_1Element(self):
		res = graph_functions.is_complete(self.g3)
		self.assertEqual(res, True, "Expected True for 1 element")

	def test_nodes_by_degree_valid(self):
		res = graph_functions.nodes_by_degree(self.g1)
		self.assertEqual(res, [('B', 3), ('A', 2), ('D', 2), ('C', 1), ('E', 0)], "Unexpected output")

	def test_nodes_by_degree_invalid(self):
		caught = False
		try:
			res = graph_functions.nodes_by_degree(self.not_a_graph)
		except TypeError:
			caught = True
		self.assertEqual(caught, True, "Expected True")
