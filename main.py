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
import sys
from graph import Graph
from queue import Queue
from stack import Stack
# OBS: Nem um dado passado como parâmetro, estranhamente, a função tem acesso aos dados de dentro do laço
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
	return graph.getID(node)

def edges(): # Cria arestas não-direcionadas no formato V1 V2 Peso
	v1, v2, weight = line.split(' ')
	graph.addEdge(v1,v2,weight)
	graph.addEdge(v2,v1,weight)

def arcs(): # Cria arestas direcionadas no formato V1 V2 Peso, onde V1 é a origem
	v1, v2, weight = line.split(' ')
	graph.addEdge(v1,v2,weight)

def queries(): # Ações no grafo
	print "Queries"

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
	except EOFError:
		#print "Entrada chegou no fim, porém, não foi encontrado marcador de fim de leitura (@)."
		#print "Programa abortado."
		break