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

from graph import Graph

obj = Graph(5)
print obj.inserirVertice()
print obj.adicionaAresta(5,4)
print obj.adicionaAresta(5,2)
print obj.adicionaAresta(5,0)
lista = obj.vizinhos(0)
if (lista == []):
	print "Sem vizinho"
else:
	print lista
print obj.removerVertice(5)
