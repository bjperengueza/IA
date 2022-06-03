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

    def agg_borde(self, nodo1, nodo2, peso=1):
       
        '''
        Añade borde al Grafo (altura y peso).
 
            Parametros:
                nodo1 (int): Un entero positivo.
                nodo2 (int): Un entero positivo.
                peso (int): Un entero positivo.
            Retorna:
                m_lista_adj (str): Lista de adyacencia agregando el valor de
                nodo1 o nodo2 y el peso.
        '''
        # Se agrega el nodo y peso en el nodo 1.
        self.m_lista_adj[nodo1].add((nodo2, peso))
 
        # Si el nodo no es dirigido.
        if not self.m_dirigido:
            # Se agrega el peso al nodo 2.
            self.m_lista_adj[nodo2].add((nodo1, peso))
            
    def ver_lista_adj(self):
 
        '''
        Imprime la representación del Grafo segun el listado de adyacencia.
        '''
        # Recorre el diccionario para implementar una lista de adyacencia.
        for key in self.m_lista_adj.keys():
            # Imprime el nodo segun la lista de adyacencia.
            print("nodo", key, ": ", self.m_lista_adj[key])