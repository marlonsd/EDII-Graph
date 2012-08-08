#coding: utf-8

"""
	// ------------------------------------------------------------
	//  Trabalho Estrutura de Dados II - Grafo
	//		Ciênia da Computação
	//
	//	Aluno: Marlon da Silva Dias
	//	GitHub: https://github.com/marlonsd/EDII-Graph
	//	main.py
	//	
	//	Main
	// ------------------------------------------------------------
"""

"""
	O que está funcionando:
		* Leitura das entradas (os *s)
		* Vertices
		* Edges
		* Arcs
		* Queries:
			- conexao
			- get
			- delete (vide Observações)
"""

"""
	Observações:
		* Único modo de terminar a execução do programa é como entrada o '@',
		caso tenha como entrada alguma forma das não já esperadas, dará erro;
		* Delete - o nodo apagado deixa de existir e puxa os seguintes ao deletado
		em uma posição.
"""
import sys
from graph import Graph
from queue import Queue
from stack import Stack

def vertices(): # Dá o nome aos vértices
	i = 0
	node = ''
	name = ''
				
	for letter in line:
		if (i == 0):
			if (letter != ' '):
				node += letter
			else:
				i = 1
		else:
			if (letter != '"'):
				name += letter

	node = int(node)
	if (node >= 0 and node < graph.getSize()):
		graph.setNode(node,name)

def edges(): # Cria arestas não-direcionadas no formato V1 V2 Peso
	v1, v2, weight = line.split(' ')
	graph.addEdge(int(v1),int(v2),int(weight)) 
	graph.addEdge(int(v2),int(v1),int(weight))

def arcs(): # Cria arestas direcionadas no formato V1 V2 Peso, onde V1 é a origem
	v1, v2, weight = line.split(' ')
	graph.addEdge(int(v1),int(v2),int(weight))

def queries(): # Ações no grafo

	op = ''
	i = 0
	
	"""
	while (line[i] != ' '):
		op += line[i]
		print i,
		i += 1
	"""

	while (True):
		try:
			if (line[i] != ' '):
				op += line[i]
				i += 1
			else:
				break
		except IndexError:
			break

	if (op == "get"):
		print graph.get(int(line[i + 1]))
	else:
		if (op == "delete"):
			print graph.delete(int(line[i + 1]))
		else:
			if (op == "vizinhos"):
				print graph.vizinhos(int(line[i + 1]))
			else:
				if (op == "conexao"):
					print graph.conexao(int(line[i + 1]), int(line[i + 3]))
				else:
					if (op == "ordemtopologica"):
						print "ordemtopologica"
					else:
						if (op == "arvoreminima"):
							graph.arvoreminima()
						else:
							if (op == "menorcaminho"):
								print "menorcaminho"
							else:
								sys.exit(0)

while (True):
	try:
		line = raw_input()

		if (line == '@'):
			break

		if (line[0] == '*'):
			number = 0
			option = ''
			for letter in line:
				if (letter != '*' and letter != ' ' and letter != '\n'):
					if (letter >= '0' and letter <= '9'):
						number = int(letter)
					else:
						option += letter
			if (option == "Vertices"):
				graph = Graph(number)
		else:
			if (option == "Vertices"):
				vertices()
			else:
				if (option == "Edges"):
					edges()
				else:
					if (option == "Arcs"):
						arcs()
					else:
						if (option == "Queries"):
							queries()
						else:
							break
	except EOFError:
		#print "Entrada chegou no fim, porém, não foi encontrado marcador de fim de leitura (@)."
		#print "Programa abortado."
		break