#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	stack.py
	//	
	//	Classe Pilha
	// ------------------------------------------------------------
"""

class Stack():

	key = []

	def __init__(self):
		self.key = []

	def __done__(self):
		self.key = []

	def push(self, element):
		self.key.insert(0, element)

	def pop(self):
		if len(self.key) > 0:
			return self.key.pop(0)

	def length(self):
		return len(self.key)

	def isEmpty(self):
		if (len(self.key) == 0):
			return true
		else:
			return false