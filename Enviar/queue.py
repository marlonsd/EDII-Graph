#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	queue.py
	//	
	//	Classe Fila
	// ------------------------------------------------------------
"""

class Queue():

	key = []

	def __init__(self):
		self.key = []

	def __done__(self):
		self.key = []

	def enqueue(self, element):
		self.key.append(element)

	def dequeue(self):
		if len(self.key) > 0:
			return self.key.pop(0)

	def leght(self):
		return len(self.key)

	def isEmpty(self):
		if (len(self.key) == 0):
			return true
		else:
			return false