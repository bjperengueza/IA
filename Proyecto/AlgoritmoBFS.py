# importación del modulo collections
from collections import deque

 

class grafo:
    '''
    Clase que representa un objeto grafico segun los datos otorgados

    '''
    # Constructor
    def __init__(self, bordes, numero_nodos):
        '''
        Contructor que inicializa el problema de busqueda

        @param bordes:  relaciona un nodo con su nodo vecino
        @param n: numero de nodos del grafo.
        
        '''
 
        # crea una lista de aristas para representar una lista de adyacencia
        self.lista_adja = [[] for _ in range(numero_nodos)]
 
        # agrega bordes al gráfico no dirigido
        for (origen, destino) in bordes:
            self.lista_adja[origen].append(destino)
            self.lista_adja[destino].append(origen)

# Realizar BFS en el gráfico a partir del vértice `v`
def BFS(grafo, v, visitado):

    '''
    Función que realiza el recorrido de busqueda en anchura
    @param v: una tupla representativa de los nodos. 
    @param visitado: estado actual del nodo de tipo boolean.

    '''
    # crea una cola para hacer la busqueda.
    q = deque()
    # marca el vértice de origen como visitado.
    visitado[v] = True
    # poner en cola el vértice fuente.
    q.append(v)

    # Bucle (whi22lrepetitivo hasta que la cola esté vacía.
    while q:
        # quitar la cola del nodo frontal e imprimirlo.
        v = q.popleft()
        print(v, end=' ')
        # do para cada arista (v, u)
        for u in grafo.lista_adja[v]:
            if not visitado[u]:
                # marcarlo como descubierto y ponerlo en cola
                visitado[u] = True
                q.append(u)