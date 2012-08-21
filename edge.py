#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	edge.py
	//	
	//	Classe Edge
	// ------------------------------------------------------------
"""

"""
	Observações:

"""
import sys
import math
from node import Node
from queue import Queue
from stack import Stack

class Edge():
	node = []
	weight = 0

	def __init__(self, start = Node(), end = Node(), weight = 0):
		self.weight = weight
		self.node += [start]
		self.node += [end]

	def __done__(self):
		self.node = []
		self.weight = -1

	def getWeight(self):
		return self.weight

	def getNode(self):
		return self.node

	def setWeight(self, weight):
		self.weight = weight

	def setNode(self, star = Node(-1), end = Node(-1)):
		if (star.getIndex() > -1):
			self.node[0] = star

		if (end.getIndex() > -1):
			self.node[0] = end

