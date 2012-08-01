#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	node.py
	//	
	//	Classe Vértice
	// ------------------------------------------------------------
"""

class Node():

	index = -1
	label = ''

	def __init__ (self, index = -1, label = ''):
		self.index = index
		self.label = label

	def __done__(self):
		self.index = -1
		self.label = ''

	def getIndex(self):
		return self.index

	def getLabel(self):
		return self.label

	def setIndex(self, index):
		self.index = index

	def setLabel(self, label):
		self.label = label