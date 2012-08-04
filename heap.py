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

"""
import sys
import math
from node import Node
from queue import Queue
from stack import Stack

class Heap():

	value = []
	size = 0

	def __init__ (self):
		value = []
		size = 0

	def __done__ (self):
		value = []
		size = 0

	def insert(self, valor):

		try:
			position = self.value.index(int(valor))
		except ValueError:
			self.value.append(int(valor))
			self.size += 1

			position = self.size
			while (position > 1):
				comp = int(math.ceil(position / 2))

				if self.value[position - 1] > self.value[comp - 1]:
					aux = self.value[position - 1]
					self.value[position - 1] = self.value[comp - 1]
					self.value[comp - 1] = aux
					position = comp
				else:
					break
	
	def change(self, valor, novo): # Valores informados a partir de 1
		try:
			position = self.value.index(int(novo))
		except ValueError:
			self.changing(valor, novo)
		

	def delete(self, valor):
		self.value[self.value.index(int(valor))] = self.value[self.size - 1]
		new = self.value[self.size - 1]
		self.value[self.size - 1] = int(valor)
		self.value.remove(int(valor))
		self.size -= 1
		self.changing(int(new),int(new))

	def changing(self, valor, novo):
		try:
			position = self.value.index(int(valor))
		except ValueError:
			position = 0

		position += 1
		
		if (position > 0):

			self.value[position - 1] = int(novo)

			comp = int(math.ceil(position / 2))
			if ((self.value[position - 1] > self.value[comp - 1]) and position > 1):
				while (position > 1):
					comp = int(math.ceil(position / 2))

					if self.value[position - 1] > self.value[comp - 1]:
						aux = self.value[position - 1]
						self.value[position - 1] = self.value[comp - 1]
						self.value[comp - 1] = aux
						position = comp
					else:
						break
			else:
				while (position <= self.size):

					try:
						son = self.value[position*2 - 1]
					except IndexError:
						son = -1

					try:
						kid = self.value[position*2]
					except IndexError:
						kid = -1

					if (son > -1 or kid > -1):

						if (son > kid):
							comp = position*2
						else:
							comp = position*2 + 1

						if self.value[position - 1] < self.value[comp - 1]:
							aux = self.value[position - 1]
							self.value[position - 1] = self.value[comp - 1]
							self.value[comp - 1] = aux
							position = comp
						else:
							break
					else:
						break

	def show(self):
		print self.value