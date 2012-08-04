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
import sys
from node import Node
from queue import Queue
from stack import Stack

"""
	* Retirar os palavrões do meio do programa
"""
class Graph():
	
	matriz = [[]]
	vertice = []
	size = 0
	node = 0
	
	def __init__(self, size = 1):
		self.size = size
		self.node = 0
		"""
		for i in range(self.size):
			node = Node(i)
			self.vertice += [node]
		"""

		for linha in range(self.size):
			self.matriz[linha] = [-1]*self.size # Certa linha recebe size vezes o [0]
			self.matriz += [[]]
			node = Node()
			self.vertice += [node]
				
		"""for linha in range(size):
			for coluna in range(size):
				print self.matriz[linha][coluna],
			print"""
			
	def __done__(self):
		self.matriz = []
		self.size = 0
		self.vertices = []
		
	def getSize(self):
		return self.size

	def getNumeroNodos(self):
		return self.node

	def setNode(self,index,label):
		if (index >= 0 and index < self.size):
			self.vertice[index].setLabel(label)
			self.vertice[index].setIndex(index)
			self.node += 1
		else:
			print "MERDA"

	def get(self,position):
		"""
			{"vertice":{"ID":1, "dado":"Fulano de Tal", "resposta":"sucesso"}}

			{"vertice":{"ID":1, "dado":"", "resposta":"falha"}}
		"""
		if (position >= 0 and position < self.size and self.node > 0):
			if (self.vertice[int(position)].getIndex() >= 0):
				index = position
			else:
				index = -1
		else:
			index = -1

		if (index >= 0):
			dado = self.vertice[int(position)].getLabel()
			resposta = "sucesso"
		else:
			dado = ''
			resposta = "falha"

		return "{\"vertice\":{\"ID\":"+str(position)+", \"dado\":\""+dado+"\", \"resposta\":\""+resposta+"\"}}"

	def delete(self, position):
		"""
			{"delete":{"ID":15,"resposta":"sucesso"}}

			{"delete":{"ID":15,"resposta":"falha"}}

		Dúvida: Quando ele é deletado, os demais deve ter o mesmo ID? Ou deve ser puxado à frente?

		"""

		if (position >= 0 and position < self.size and self.node > 0):
			if (self.vertice[int(position)].getIndex() >= 0):
				index = position
			else:
				index = -1
		else:
			index = -1

		if (index >= 0):
			self.matriz.remove(self.matriz[position]) # Remove toda a linha a
			self.size -= 1
			self.node -= 1
			self.vertice[position + 1].setIndex(self.vertice[position].getIndex())
			del self.vertice[position]
			
			for i in range(self.size):
				del self.matriz [i][position] # Remove a coluna a em todas as linhas
				"""if (i >= position):
					self.vertice[i].setIndex(i)"""
			resposta = "sucesso"
		else:
			resposta = "falha"

		return "{\"delete\":{\"ID\":"+str(position)+",\"resposta\":\""+resposta+"\"}}"

	def vizinhos(self, position):
		"""
		{"vizinhos":{"ID":1, "resposta":"sucesso", "vizinhos":[0,2,1]}}

		{"vizinhos":{"ID":1, "resposta":"falha", "vizinhos":[]}}
		"""
		lista = []
		
		if (position >= 0 and position < self.size):
			resposta = "sucesso"
			for i in range(self.size):
				if (self.matriz[position][i] > -1):
					lista += [i]
		else:
			lista = []
			resposta = "falha"
		
		return "{\"vizinhos\":{\"ID\":"+str(position)+",\"resposta\":\""+resposta+"\", \"vizinhos\":"+str(lista)+"}}"


	def conexao(self, a, b): #B é adjacente a A (existe A -> B)
		"""
		Se existe uma conexão, independênte de dirigida ou não?

		Se a conexão não existe, informar não?
		{"conexao":{"ID1":0, "ID2":1, "resposta":"sucesso", "conexao":"sim"}}

		{"conexao":{"ID1":0, "ID2":1, "resposta":"falha", "conexao":""}}
		"""

		conexao = ''

		if a < self.size and b < self.size:
			resposta = "sucesso"
			if (self.matriz[a][b] > -1) :
				conexao = "sim"
			else:
				conexao = "nao"
		else:
			resposta = "falha"

		return "{\"conexao\":{\"ID\":"+str(a)+", \"ID2\":"+str(b)+", \"resposta\":\""+resposta+"\", \"conexao\":\""+conexao+"\"}}"

	def arvoreminima(self):
		"""
			{"arvoreminima":{"arestas":[(1,2),(2,0),(1,0)], "custo":21}}
		"""

	def addEdge(self, a, b, weight):
		"""
			O que fazer se a aresta já existir?
		"""
		if (a >= 0 and a < self.size) and (b >= 0 and b < self.size):
			self.matriz[a][b] = weight
			return True
		else:
			return False
			
	def removeEdge(self, a, b):
		if (a >= 0 and b >= 0) and (a < self.size and b < self.size):
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
		
		
	def buscaAmplitude(self,origin,destination):
		position = origin
		checked = []
		queue = Queue()

		if (position == destination):
			return True
		checked.append(position)
		queue.enqueue(position)

		while(not queue.isEmpty()):
			position = queue.dequeue()
			if (position == destination):
				return True
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
						return True
					checked.append(position)
					queue.enqueue(position)

		return False

	def buscaAmplitude(self,origin,destination):
		position = origin
		checked = []
		stack = Stack()

		if (position == destination):
			return True
		checked.append(position)
		stack.push(position)

		while(not queue.isEmpty()):
			position = stack.pop()
			if (position == destination):
				return True
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
						return True
					checked.append(position)
					stack.push(position)

		return False