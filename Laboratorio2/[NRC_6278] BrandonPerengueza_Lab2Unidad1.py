# Inportación del modulo Queue.
from queue import Queue

class Grafo:
    '''Establece la funcionalidad del Algoritmo de Busqueda en Anchura.'''
    # Constructor
    def __init__(self, num_nodos, dirigido=True):

        ''' 
        Crea el objeto con los atributos y metodos, verifica si los nodos son dirigidos e 
        implementa una lista de adyacencia.

            Parametros:
                m_num_nodos (int): Un entero positivo.
                dirigido (boolean): Verdadero o falso.
            Retorna:
                m_lista_adj (str): Lista de adyacencia.
        '''
        
        # Con el Metodo "self" se accede a los atributos y enlaza 
        # con los argumentos necesarios.
        self.m_num_nodos = num_nodos
        self.m_nodos = range(self.m_num_nodos)
		
        # Dirigido o no dirigido.
        self.m_dirigido = dirigido
		
        # Representación de Grafo - Lista de adyacencia.
        # Utilizamos un diccionario para implementar una lista de adyacencia.
        self.m_lista_adj = {nodo: set() for nodo in self.m_nodos}      
	
