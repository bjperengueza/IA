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
        for i in self.m_lista_adj.keys():
            # Imprime el nodo segun la lista de adyacencia.
            print("nodo", i, ": ", self.m_lista_adj[i])

    def ba_transversal(self, iniciar_nodo):

        ''' 
        Función que imprime el recorrido BA (Busqueda en Anchura) a partir de un vértice fuente dado.
        Recorre los vértices alcanzables desde s.
            
            Parametros:
                iniciar_nodo (str): inicializa el nodo para su recorrido. 

            Retorna:
                nodo_nuevo (str): nodo vecino que se va a visitar.

        ''' 

        # Conjunto de nodos visitados para evitar bucles.
        visitado = set()
        queue = Queue()

        # Añadir el iniciar_nodo a la lista de cola. 
        queue.put(iniciar_nodo)
        # Añadir el iniciar_nodo a la lista de visitado.
        visitado.add(iniciar_nodo)

        # Mientras la cola no este vacia. 
        while not queue.empty():
            # Descola a un vértice de cola. 
            nodo_actual = queue.get()
            # Imprime el vertice.
            print(nodo_actual, end = " ")

            # Obtener todos los vértices adyacentes del vértice de la cola.   
            for (nodo_nuevo, peso) in self.m_lista_adj[nodo_actual]:
                # Si un vértice adyacente no ha sido visitado.
                if nodo_nuevo not in visitado:
                    # Marcado como en cola.
                    queue.put(nodo_nuevo)
                    # Marcado como visitado.
                    visitado.add(nodo_nuevo)