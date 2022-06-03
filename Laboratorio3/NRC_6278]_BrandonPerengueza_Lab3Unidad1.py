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

    def dfs(self, iniciar, objetivo, ruta = [], visitado = set()):

        ''' 
        Función que imprime el recorrido BP (Busqueda en Profundidad) a partir de un vértice fuente dado.
        Recorre los vértices alcanzables desde s.
            
            Parametros:
                iniciar (str): inicializa el nodo para su recorrido. 

            Retorna:
                resultado (str): nodo vecino que se va a visitar.

        ''' 
        # Añadir el iniciar a la lista de la ruta.
        ruta.append(iniciar)
        # Añadir el iniciar a la lista de visitado.
        visitado.add(iniciar)
        # Si iniciar es igual a objetivo
        if iniciar == objetivo:
            # Retorna la ruta de nodos
            return ruta
        # Se establece el nodo vecino y el peso en la lista de adyacencia
        for (n_vecino, peso) in self.m_lista_adj[iniciar]:
            # Si el nodo vecino no a sido visitado
            if n_vecino not in visitado:
                # Se llama a la funcion de forma recursiva
                resultado = self.dfs(n_vecino, objetivo, ruta, visitado)
                # Si el resultado no se encontro
                if resultado is not None:
                    # Retorna la ruta transversal
                    return resultado
        # Las ramas vecinas del nodo actual han sido visitadas
        ruta.pop()
        return None

if __name__ == "__main__":
 
    ''' 
    Crea una instancia de la clase "Grafo"
    El grafo sera no dirigido y contara con n nodos y n asintoras segun las que el usuario ingrese
    Imprimira la lista de adyacencia de la forma:
        
        Parametros:
            cant_nodos (int): Un entero positivo
            cant_aristas(int): Un entero positivo

        
        Retorna:
            graf_1 (str): ruta transversal 

    '''
 
     # Mensaje de Inicio
    print(" ")
    print("************************ BUSQUEDA EN PROFUNDIDAD (DFS) ************************")
    print(" ")
 
    # Ingresa la cantidad de nodos.
    # transforma a tipo de dato entero.
    cant_nodos = int(input("Ingrese la cantidad de nodos: "))
    cant_aristas = int(input("Ingrese la cantidad de aristas: "))
    print(" ")

    # Instancia la clase "Grafo" con los valores respectivos.
    graf_1 = Grafo(cant_nodos, dirigido=False)
 
    # Recorre una variable en un rango de 0 hasta la cantidad de nodos ingresados.
    for s in range (0, cant_aristas ):
 
        # Solicita el primer dato de la clase "Grafo".
        nodo_inicio = int(input("Digite el nodo de inicio: "))
        # Solicita el segundo dato de la clase "Grafo".
        nodo_destin = int(input("Digite el nodo de destino: "))
        # Agrega los dos valores a la clase "Grafo".
        graf_1.agg_borde(nodo_inicio, nodo_destin)
        # Numero de arista
        print ("Arista ", s)
 
    print("")
    print("Ingrese la ruta que deseé buscar.")
    rut_inicio = int(input("Ingrese el nodo de partida: "))
    rut_llegada = int(input("Ingrese el nodo de llegada: "))
    print("")
 
    # Imprime la lista de adyacencia en la forma nodo n: {(nodo, peso)}
    graf_1.ver_lista_adj()

    # Imprime la ruta transversal del nodo
    ruta_transversal = []
    ruta_transversal = graf_1.dfs(rut_inicio, rut_llegada)
    print(f" La ruta transversal del nodo raiz al nodo destino es: {ruta_transversal}")