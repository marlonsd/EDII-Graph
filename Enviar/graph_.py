#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//			Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	graph.py
	//	
	//	Classe Grafo
	//  w/ Heap
	// ------------------------------------------------------------
"""
import sys
from node import Node
from heap_ import Heap
from tree import Tree
from queue import Queue
from stack import Stack

class Graph():
	
	matriz = [[]]
	vertice = []
	size = 0
	node = 0
	edge = 0
	
	def __init__(self, size = 1):
		self.size = size
		self.node = 0

		for linha in range(self.size):
			self.matriz[linha] = [-1]*self.size # Certa linha recebe size vezes o [0]
			self.matriz += [[]]
			node = Node()
			self.vertice += [node]
		edge = 0
			
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
			if (self.vertice[index].getIndex() == -1):
				self.node += 1
			self.vertice[index].setLabel(label)
			self.vertice[index].setIndex(index)

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
			resposta = "sucesso"
		else:
			resposta = "falha"

		return "{\"delete\":{\"ID\":"+str(position)+", \"resposta\":\""+resposta+"\"}}"

	def vizinhos(self, position):
		"""
		{"vizinhos":{"ID":1, "resposta":"sucesso", "vizinhos":[0,2,1]}}

		{"vizinhos":{"ID":1, "resposta":"falha", "vizinhos":[]}}
		"""
		lista = []
		
		if (position >= 0 and position < self.size):
			for i in range(self.size):
				if (self.matriz[position][i] > -1):
					lista += [i]
			if (len(lista) > 0):
				resposta = "sucesso"
				out = "["
				for i in range(len(lista)):
					if (i < (len(lista) - 1)):
						out += str(lista[i])+str(',')
					else:
						out += str(lista[i])+str(']')
			else:
				out = []
				resposta = "falha"
		else:
			out = []
			resposta = "falha"
		
		return "{\"vizinhos\":{\"ID\":"+str(position)+", \"resposta\":\""+resposta+"\", \"vizinhos\":"+str(out)+"}}"


	def conexao(self, a, b): #B é adjacente a A (existe A -> B)
		"""
		{"conexao":{"ID1":0, "ID2":1, "resposta":"sucesso", "conexao":"sim"}}

		{"conexao":{"ID1":0, "ID2":1, "resposta":"falha", "conexao":""}}
		"""

		conexao = ''
		resposta = "falha"
		if a < self.size and b < self.size:
			if (self.buscaEmProfundidade(a,b)):
				conexao = "sim"
				resposta = "sucesso"

		return "{\"conexao\":{\"ID\":"+str(a)+", \"ID2\":"+str(b)+", \"resposta\":\""+resposta+"\", \"conexao\":\""+conexao+"\"}}"

	def arvoreminima(self):
		"""
			Opera apenas em grafos não-direcionados e conectados
			{"arvoreminima":{"arestas":[(1,2),(2,0),(1,0)], "custo":21}}

			{"arvoreminima":{"arestas":[(3,4),(1,2),(0,1),(2,3)], "custo":18}}

		"""

		copy = self.matriz
		edges = Heap()
		menor = [-1,-1,-1]

		teste = False

		out = []
		weight = ''
		"""
		for k in range (self.edge/2):
			for i in range (self.size):
				for j in range (i):
					if (copy[i][j] > -1):
						if (int(menor[2]) > int(-1)):
							if (int(copy[i][j]) < int(menor[2])):
								menor = [j,i,copy[i][j]]
								teste = True
						else:
							menor = [j,i,copy[i][j]]
							teste = True

			copy[menor[1]][menor[0]] = -1
			edges += [menor]
			menor = [-1,-1,-1]
		"""

		for i in range(self.size):
			for j in range (i):
				if (self.matriz[i][j] > -1):
					edges.insert([j,i,self.matriz[i][j]])
					teste = True

		#edges.show()

		if teste:
			connected = Tree(self.size)
			aux = edges.pop()

			weight = aux[2]
			tree = [[aux[0],aux[1]]]
			#print aux,connected.find(aux[0]),connected.find(aux[1])
			connected.merge(aux[0],aux[1])

			while (len(tree) < self.size - 1):
				aux = edges.pop()

				if (connected.find(aux[0]) != connected.find(aux[1])):
					#print aux,connected.find(aux[0]),connected.find(aux[1])
					weight += aux[2]
					tree += [[aux[0],aux[1]]]
					connected.merge(aux[0],aux[1])

			out = "["
			for i in range(len(tree)):
				out += str("(")+str(tree[i][0])+","+str(tree[i][1])+")"
				if (i < (len(tree) - 1)):
					out += str(',')
			out += "]"

		return "{\"arvoreminima\":{\"arestas\":"+str(out)+", \"custo\":"+str(weight)+"}}"
		
	def menorcaminho(self, a, b):
		"""
			{"menorcaminho":{"ID1":0, "ID2":3, "caminho":[0,2,5,4,3], "custo":17}}
			'a' representa infinito
		"""

		out = []
		custo = ''

		dist = []
		for i in range(self.size):
			dist += [['a',[]]]

		dist[int(a)][0] = 0
		dist[int(a)][1] = [int(a)]

		q = []
		for i in range(self.size):
			q += [i]

		caminho = []

		while (len(q) > 0):
			none = True
			menor = 'a'
			for i in range (len(dist)):
				if (dist[i][0] != 'a'):

					try:
						aux = q.index(i)
					except ValueError:
						aux = -1

					if (aux > -1):
						if (menor != 'a'):

							if (dist[i][0] < menor):
								menor = dist[i][0]
								u = i
								none = False
						else:
							menor = dist[i][0]
							u = i
							none = False
			
			if none:
				break
			q.remove(int(u))
			
			for i in range (self.size):

				if (self.matriz[u][i] > -1):
					alt = dist[u][0] + self.matriz[u][i]
					caminho = dist[u][1]
					if (dist[i][0] != 'a'):
						if alt < dist[i][0]:
							dist[i][0] = alt
							dist[i][1] = dist[u][1] + [int(i)] 
					else:
						dist[i][0] = alt
						dist[i][1] = dist[u][1] + [int(i)]

		custo = dist[int(b)][0]

		if (dist[int(b)][0] == 'a'):
			custo = ''

		out = "["
		i = 0
		
		while (i < len(dist[int(b)][1])):
			out += str(dist[int(b)][1][i])
			i += 1
			if (i < len(dist[int(b)][1])):
				out += str(',')

		out += "]"

		return "{\"menorcaminho\":{\"ID1\":"+str(a)+", \"ID2\":"+str(b)+", \"caminho\":"+str(out)+",\"custo\":"+str(custo)+"}}"

	def ordemtopologica(self):
		"""
			{"ordemtop":[1,2,0]}
		"""
		out = []

		ordemtop = []
		edges = self.matriz
		tryout = False
		while (len(ordemtop) < self.node):
			#print "----"
			toDelete = []
			for coluna in range(self.size):
				#print "*****"
				if (self.vertice[coluna].getIndex() > -1):
					try:
						i = ordemtop.index(coluna)
					except ValueError:
						tryout = True
						for linha in range(self.size):
							if (self.vertice[linha].getIndex() > -1):
								#print linha, coluna, edges[linha][coluna],"\t", self.matriz[linha][coluna]
								if (edges[linha][coluna] > -1):
									tryout = False
									break
						if tryout:
							ordemtop += [coluna]
							toDelete += [coluna]
				#print "*****"
			for i in range (len(toDelete)):
				for j in range(self.size):
					edges[toDelete[i]][j] = -1
			#print "----"
			
		if tryout:
			for i in range(self.node):
				for j in range(self.node):
					if (edges[i][j] > -1):
						tryout = False
						break

		if tryout:
			out = "["
			for i in range(len(ordemtop)):
				out += str(ordemtop[i])
				if (i < (len(ordemtop) - 1)):
					out += str(',')
			out += "]"

		return "{\"ordemtop\":"+str(out)+"}"

	def addEdge(self, a, b, weight):
		if (a >= 0 and a < self.size) and (b >= 0 and b < self.size):
			if (self.matriz[a][b] == -1):
				self.edge += 1
			self.matriz[a][b] = weight
			return True
		else:
			return False

	def buscaEmProfundidade(self, a, b):

		pilha = Stack()
		if (a < len(self.matriz)):
			pilha.push(a)
			answer = [a]
			while (pilha.length() > 0):
				i = pilha.pop()
				j = 0
				check = True
				while j < self.size and check:
					if (self.matriz[i][j] > -1):
						if (j == b):
							return True
						try:
							aux = answer.index(j)
						except ValueError:
							answer += [j]
							pilha.push(i)
							pilha.push(j)
							check = False
					j += 1

		return False