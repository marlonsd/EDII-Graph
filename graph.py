#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	graph.py
	//	
	//	Classe Grafo
	// ------------------------------------------------------------
"""
from queue import Queue
from stack import Stack

class Graph():
	
	matriz = [[]]
	size = 0
	
	def __init__(self, size = 1):
		self.size = size
				
		for linha in range(size):
			self.matriz[linha] = [0]*size # Certa linha recebe size vezes o [0]
			self.matriz += [[]]
				
		"""for linha in range(size):
			for coluna in range(size):
				print self.matriz[linha][coluna],
			print"""
			
	def __done__(self):
		matriz = []
		size = 0
		
	def addEdge(self, a, b):
		if a < self.size and b < self.size:
			self.matriz[a][b] = 1
			return True
		else:
			return False
			
	def removeEdge(self, a, b):
		if a < self.size and b < self.size:
			self.matriz[a][b] = 0
			return True
		else:
			return False
		
	def addNode(self):
		
		"""
			Em cada linha adiciona uma nova coluna vazia ( [] )
		"""
		for i in range(self.size):
			self.matriz[i] += [[]]
		
		self.matriz += [[]] # Adicina uma nova linha, contendo somente []
		self.size += 1
		
		self.matriz[self.size - 1] = [0]*self.size
		
		"""
			Percorre a matriz.
				Em cada linha (var: linha) na sua última coluna (self.size - 1) troca o valor por 0
		"""
		for linha in range(self.size):
			self.matriz[linha][self.size - 1] = 0
					
		return True
		
	def removeNode(self, a):
		if a > 0 and a < self.size:
			self.matriz.remove(self.matriz[a]) # Remove toda a linha a
			self.size -= 1
			
			for i in range(self.size):
				del self.matriz [i][a] # Remove a coluna a em todas as linhas
				
			return True
		else:
			return False
				
	def neighbors(self, a):
		lista = []
		
		for i in range(self.size):
			if (self.matriz[a][i] == 1):
				lista += [i]
			
		return lista
		
	def checkAdjacency(self, a, b): #B é adjacente a A (existe A -> B)
		if a < self.size and b < self.size:
			if self.matriz[b][a] == 1 :
				return True
			else:
				return False
		else:
			return False

	def buscaAmplitude(self,origin,destination):
		position = origin
		checked = []
		queue = Queue()

		if (position == destination):
			return true
		checked.append(position)
		queue.enqueue(position)

		while(!queue.isEmpty()):
			position = queue.dequeue()
			if (position == destination):
				return true
			checked.append(position)

			neighbors = self.neighbors(position)
			while(len(neighbors) != 0):
				position = neighbors.pop(0)

				try:
					i = checked.index(position)
				except ValueError:
					i = -1

				if (i == -1):
					if (position == destination):
						return true
					checked.append(position)
					queue.enqueue(position)

	def buscaAmplitude(self,origin,destination):
		position = origin
		checked = []
		stack = Stack()

		if (position == destination):
			return true
		checked.append(position)
		stack.push(position)

		while(!queue.isEmpty()):
			position = stack.pop()
			if (position == destination):
				return true
			checked.append(position)

			neighbors = self.neighbors(position)
			while(len(neighbors) != 0):
				position = neighbors.pop(0)

				try:
					i = checked.index(position)
				except ValueError:
					i = -1

				if (i == -1):
					if (position == destination):
						return true
					checked.append(position)
					stack.push(position)