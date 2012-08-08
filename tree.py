#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	tree.py
	//	
	//	Classe Tree
	//		Classe auxiliar utilizada na formação da Árvore Mínima
	// ------------------------------------------------------------
"""

"""
	Observações:

"""

class Tree():

	tree = []
	size = 0

	def __init__ (self, size = 0):
		self.size = size
		for i in range(self.size):
			self.tree += [i]

	def __done__ (self):
		tree = []
		size = 0

	def find(self, indice):
		i = indice
		while (not self.tree[i] == i):
			i = self.tree[i]

		return self.tree[i]

	def merge(self, v, u):
		if (u > v):
			self.tree[u] = self.tree[v]
		else:
			self.tree[v] = self.tree[u]