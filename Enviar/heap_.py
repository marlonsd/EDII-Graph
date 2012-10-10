#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	heap.py
	//	
	//	Classe Heap
	// ------------------------------------------------------------
"""

"""
	Observações:
		- Começa do 1 a contagem dos elementos da árvore (no vetor)
		- NÃO suporta valores repetidos, se tiver um valor e tentar
		ser inserido um mesmo, simplesmente será ignorado a adição

		* Como parâmtro das funções, é espero que se passe um "edge"

"""
import sys
import math
from node import Node
from edge import Edge
from queue import Queue
from stack import Stack

class Heap():

	value = [] # [PESO, [VÉRTICE 1, VÉRTICE 2]]
	size = 0

	def __init__ (self):
		value = []
		size = 0

	def __done__ (self):
		value = []
		size = 0

	def insert(self, valor):

		# Rejeitando Números Repetidos
		"""
		try:
			position = self.value.index(int(valor))
		except ValueError:
			self.value.append(int(valor))
			self.size += 1

			position = self.size
			while (position > 1):
				comp = int(math.ceil(position / 2))

				if self.value[position - 1] < self.value[comp - 1]:
					aux = self.value[position - 1]
					self.value[position - 1] = self.value[comp - 1]
					self.value[comp - 1] = aux
					position = comp
				else:
					break

		"""

		# Aceitando números repetidos

		self.value.append(valor)
		self.size += 1

		position = self.size
		while (position > 1):
			comp = int(math.ceil(position / 2))

			if self.value[position - 1][2] < self.value[comp - 1][2]:
				aux = self.value[position - 1]
				self.value[position - 1] = self.value[comp - 1]
				self.value[comp - 1] = aux
				position = comp
			else:
				break
	
	def change(self, valor, novo): # Valores informados a partir de 1
		try:
			position = self.value.index(novo)
		except ValueError:
			self.changing(valor, novo)
		

	def delete(self, valor):
		#print "Delete: "+str(valor[2])
		#print self.value[self.size - 1][2]
		self.value[self.value.index(valor)] = self.value[self.size - 1]
		new = self.value[self.size - 1]
		self.value[self.size - 1] = valor
		self.value.remove(valor)
		self.size -= 1
		self.changing(new,new)

	def pop(self):
		if (self.size > 0):
			pop = self.value[0]
			self.delete(self.value[0])
			return pop

	def changing(self, valor, novo):
		try:
			position = self.value.index(valor)
		except ValueError:
			position = 0

		position += 1
	
		if (position > 0):

			self.value[position - 1] = novo

			comp = int(math.ceil(position / 2))
			#print position, comp
			if (position > 1 and (self.value[position - 1][2] < self.value[comp - 1][2])):
				while(position > 1):
					comp = int(math.ceil(position / 2))

					if self.value[position - 1][2] < self.value[comp - 1][2]:
						aux = self.value[position - 1]
						self.value[position - 1] = self.value[comp - 1]
						self.value[comp - 1] = aux
						position = comp
					else:
						break
			else:
				while(position <= self.size):

					try:
						son = self.value[position*2 - 1][2]
						#print "son "+str(self.value[position*2 - 1][2])
					except IndexError:
						son = -1

					try:
						kid = self.value[position*2][2]
						#print "kid "+str(self.value[position*2][2])
					except IndexError:
						kid = -1

					comp = 0

					if (son < 0):
						comp = position*2
					else:
						if (kid < 0):
							comp = position*2 - 1
						else:
							if (son <= kid):
								comp = position*2
							else:
								comp = position*2 + 1
					#print position, comp
					if (comp > 0 and comp <= self.size):
						if self.value[position - 1][2] > self.value[comp - 1][2]:
							aux = self.value[position - 1]
							self.value[position - 1] = self.value[comp - 1]
							self.value[comp - 1] = aux
							position = comp
						else:
							break
					else:
						break

			"""
			else:
							

					if (son > -1 or kid > -1):

						if (son < kid):
							comp = position*2
						else:
							comp = position*2 + 1
						#print str(self.value[comp - 1][2])
						print comp
						if self.value[position - 1][2] > self.value[comp - 1][2]:
							aux = self.value[position - 1]
							self.value[position - 1] = self.value[comp - 1]
							self.value[comp - 1] = aux
							position = comp
						else:
							break
					else:
						break"""

	def show(self):
		print self.value