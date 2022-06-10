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
