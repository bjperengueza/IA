""" 
    Universidad de las Fuerzas Armadas ESPE Sede Santo Domingo de los Colorados
    Departamento Ciencias de la Computación
    Ingeniería en Tecnologías de la Información
    
    Autores: José Ruiz
             Brandon Perengueza
    Materia: Inteligencia Artificial
    Programación del Algoritmo de Busqueda en Anchura
    Agente: Agrobot E-Series cosechador de fresas
"""


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

    # Bucle (while repetitivo hasta que la cola esté vacía).
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

if __name__ == '__main__':

    '''
    Clase principal donde se ejecutaran las funciones previamente creadas

    '''
 
    # Lista de bordes de gráficos según el diagrama anterior
    print("")
    print("********************** RECORRIDO DE LAS PARCELAS **********************")
    print("")

    # Lista de bordes de gráficos según el grafo establecido
    bordes = [
         (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 11), (5, 12), (6, 13), (3, 7), (3, 8), (7, 14),
         (7, 15), (8, 16), (8, 17), (4, 9), (4, 10), (9, 18), (9, 19), (10, 20),
    ]

    
    print("")
    # imprime la lista de parcelas relacionadas
    print("Las Rutas de las Parcelas son las siguientes:")
    print(bordes)

    # número total de parcelas que se busca recorrer
    n = int(input("Ingrese el total de parcelas que desea recorrer: "))
    print("")

    # parcela inicial desde donde se desea iniciar el recorrido
    inic = int(input("Ingrese la parcela inicial: "))
    print("")

    # construye un gráfico a partir de los bordes dados
    grafo = grafo(bordes, n)
 
    # para realizar un seguimiento de si se descubre un vértice o no
    visitado = [False] * n
 
    # Realizar el recorrido BFS de todos los nodos no visitados y
    # cubre todos los componentes conectados de un gráfico
    if not visitado[inic]:
        # inicia el recorrido BFS desde el vértice inic
        print("El recorrido a realizar es el siguiente:")
        BFS(grafo, inic, visitado)