# -*- coding: latin1 -*-
class Graph():
	
	matriz = [[]]
	size = 0
	
	def __init__(self, size):
		self.size = size
				
		for linha in range(size):
			for coluna in range(size):
				self.matriz[linha] += [0]
			self.matriz += [[]]
				
		"""for linha in range(size):
			for coluna in range(size):
				print self.matriz[linha][coluna],
			print"""
			
	def __done__(self):
		matriz = {}
		size = 0
		
	def adicionaAresta(self, a, b):
		if a < self.size and b < self.size:
			self.matriz[a][b] = 1
			return True
		else:
			return False
		
	def verificaAdjacencia(self, a, b): #B é adjacente a A (existe A -> B)
		if a < self.size and b < self.size:
			if self.matriz[b][a] == 1 :
				return True
			else:
				return False
		else:
			return False

obj = Graph(5)
print obj.adicionaAresta(4,5)
print obj.adicionaAresta(4,3)
print obj.verificaAdjacencia(3, 4)
print obj.verificaAdjacencia(4, 3)
