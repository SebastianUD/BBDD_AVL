from typing import Optional
from Estudiante import Estudiante
from NodoAVL import NodoAVL
from binarytree import Node as BinaryTreeNode


# Árbol AVL completo con todas las operaciones
class ArbolAVL:
    def __init__(self):
        """
        Este método será responsable de inicializar un nuevo árbol AVL vacío

        """
        self.raiz: Optional[NodoAVL] = None

    def obtener_altura(self, nodo: Optional[NodoAVL]) -> int:
        """
        Este método será responsable de obtener la altura de un nodo

        Args:
            nodo (Optional[NodoAVL]): El nodo del cual se desea obtener la altura

        Returns:
            int: La altura del nodo, 0 si el nodo es None
        """
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo: Optional[NodoAVL]) -> int:
        """
        Este método será responsable de calcular el factor de balance de un nodo

        Args:
            nodo (Optional[NodoAVL]): El nodo del cual se desea calcular el balance

        Returns:
            int: El factor de balance (altura derecha - altura izquierda), 0 si el nodo es None
        """
        return self.obtener_altura(nodo.derecha) - self.obtener_altura(nodo.izquierda) if nodo else 0

    def actualizar_altura(self, nodo: NodoAVL):
        """
        Este método será responsable de actualizar la altura de un nodo basándose en sus hijos

        Args:
            nodo (NodoAVL): El nodo cuya altura se desea actualizar
        """
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

    def rotacion_derecha(self, y: NodoAVL) -> NodoAVL:
        """
        Este método será responsable de realizar una rotación derecha en el árbol AVL

        Args:
            y (NodoAVL): El nodo raíz del subárbol que se va a rotar

        Returns:
            NodoAVL: El nuevo nodo raíz después de la rotación
        """
        x = y.izquierda
        T2 = x.derecha
        
        # Realizar rotación
        x.derecha = y
        y.izquierda = T2
        
        # Actualizar alturas
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        
        print(f"[BALANCEO] Rotación derecha en nodo {y.estudiante.codigo}")
        return x

    def rotacion_izquierda(self, x: NodoAVL) -> NodoAVL:
        """
        Este método será responsable de realizar una rotación izquierda en el árbol AVL

        Args:
            x (NodoAVL): El nodo raíz del subárbol que se va a rotar

        Returns:
            NodoAVL: El nuevo nodo raíz después de la rotación
        """
        y = x.derecha
        T2 = y.izquierda
        
        # Realizar rotación
        y.izquierda = x
        x.derecha = T2
        
        # Actualizar alturas
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        
        print(f"[BALANCEO] Rotación izquierda en nodo {x.estudiante.codigo}")
        return y

    def balancear_nodo(self, nodo: NodoAVL, codigo: int) -> NodoAVL:
        """
        Este método será responsable de balancear un nodo si es necesario después de inserción/eliminación

        Args:
            nodo (NodoAVL): El nodo que se va a balancear
            codigo (int): El código del estudiante que se insertó/eliminó para determinar el tipo de rotación

        Returns:
            NodoAVL: El nodo balanceado (puede ser el mismo nodo si no necesitaba balanceo)
        """
        balance = self.obtener_balance(nodo)
        
        if abs(balance) > 1:
            print(f"[BALANCE] Nodo {nodo.estudiante.codigo} tiene balance {balance}")
        
        # Caso Izquierda-Izquierda
        if balance < -1 and codigo < nodo.izquierda.estudiante.codigo:
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Derecha
        if balance > 1 and codigo > nodo.derecha.estudiante.codigo:
            return self.rotacion_izquierda(nodo)
        
        # Caso Izquierda-Derecha
        if balance < -1 and codigo > nodo.izquierda.estudiante.codigo:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Izquierda
        if balance > 1 and codigo < nodo.derecha.estudiante.codigo:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)
        
        return nodo

    def insertar(self, nodo: Optional[NodoAVL], estudiante: Estudiante, mostrar_mensajes: bool = True) -> NodoAVL:
        """
        Este método será responsable de insertar un nuevo estudiante en el árbol AVL

        Args:
            nodo (Optional[NodoAVL]): El nodo actual donde se intenta insertar
            estudiante (Estudiante): El estudiante que se va a insertar
            mostrar_mensajes (bool): Si se deben mostrar mensajes de debug durante la inserción

        Returns:
            NodoAVL: El nodo raíz del subárbol después de la inserción y balanceo
        """
        # Inserción normal BST
        if not nodo:
            if mostrar_mensajes:
                print(f"[INSERCIÓN] Nuevo nodo creado con código {estudiante.codigo}")
            return NodoAVL(estudiante)

        if estudiante.codigo < nodo.estudiante.codigo:
            nodo.izquierda = self.insertar(nodo.izquierda, estudiante, mostrar_mensajes)
        elif estudiante.codigo > nodo.estudiante.codigo:
            nodo.derecha = self.insertar(nodo.derecha, estudiante, mostrar_mensajes)
        else:
            if mostrar_mensajes:
                print(f"[ADVERTENCIA] Código {estudiante.codigo} ya existe. No se insertó.")
            return nodo

        # Actualizar altura y balancear
        self.actualizar_altura(nodo)
        return self.balancear_nodo(nodo, estudiante.codigo)

    def obtener_maximo_valor_nodo(self, nodo: NodoAVL) -> NodoAVL:
        """
        Este método encontrará el nodo con el valor máximo en el subárbol

        Args:
            nodo (NodoAVL): El nodo raíz del subárbol donde buscar el máximo

        Returns:
            NodoAVL: El nodo que contiene el valor máximo
        """
        while nodo.derecha:
            nodo = nodo.derecha
        return nodo

    def eliminar(self, nodo: Optional[NodoAVL], codigo: int) -> Optional[NodoAVL]:
        """
        Este método será responsable de eliminar un estudiante del árbol AVL

        Args:
            nodo (Optional[NodoAVL]): El nodo actual donde se busca el estudiante a eliminar
            codigo (int): El código del estudiante que se va a eliminar

        Returns:
            Optional[NodoAVL]: El nodo raíz del subárbol después de la eliminación y balanceo
        """
        if not nodo:
            print(f"[ADVERTENCIA] Código {codigo} no encontrado para eliminar.")
            return nodo

        # Búsqueda del nodo a eliminar
        if codigo < nodo.estudiante.codigo:
            nodo.izquierda = self.eliminar(nodo.izquierda, codigo)
        elif codigo > nodo.estudiante.codigo:
            nodo.derecha = self.eliminar(nodo.derecha, codigo)
        else:
            print(f"[ELIMINACIÓN] Eliminando nodo con código {codigo}")
            
            # Nodo con un hijo o sin hijos
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            
            # Nodo con dos hijos: obtener el predecesor
            temp = self.obtener_maximo_valor_nodo(nodo.izquierda)
            nodo.estudiante = temp.estudiante
            nodo.izquierda = self.eliminar(nodo.izquierda, temp.estudiante.codigo)

        # Actualizar altura
        self.actualizar_altura(nodo)
        
        # Balancear el árbol
        balance = self.obtener_balance(nodo)
        
        if abs(balance) > 1:
            print(f"[BALANCE] Nodo {nodo.estudiante.codigo} tiene balance {balance}")

        # Casos de balanceo
        if balance < -1:
            if self.obtener_balance(nodo.izquierda) <= 0:
                return self.rotacion_derecha(nodo)
            else:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo)
        
        if balance > 1:
            if self.obtener_balance(nodo.derecha) >= 0:
                return self.rotacion_izquierda(nodo)
            else:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo)

        return nodo

    def agregar_estudiante(self, estudiante: Estudiante):
        """
        Este método será responsable de agregar un estudiante al árbol AVL

        Args:
            estudiante (Estudiante): El estudiante que se va a agregar al árbol
        """
        print(f"\n[OPERACIÓN] Insertando estudiante con código {estudiante.codigo}")
        self.raiz = self.insertar(self.raiz, estudiante)

    def eliminar_estudiante(self, codigo: int):
        """
        Este método será responsable de eliminar un estudiante del árbol AVL

        Args:
            codigo (int): El código del estudiante que se va a eliminar
        """
        print(f"\n[OPERACIÓN] Eliminando estudiante con código {codigo}")
        self.raiz = self.eliminar(self.raiz, codigo)

    def actualizar_estudiante(self, codigo: int, nuevo_estudiante: Estudiante):
        """
        Este método será responsable de actualizar un estudiante eliminando el antiguo e insertando el nuevo

        Args:
            codigo (int): El código del estudiante que se va a actualizar
            nuevo_estudiante (Estudiante): Los nuevos datos del estudiante
        """
        print(f"\n[OPERACIÓN] Actualizando estudiante con código {codigo}")
        self.raiz = self.eliminar(self.raiz, codigo)
        self.raiz = self.insertar(self.raiz, nuevo_estudiante)
        if codigo == nuevo_estudiante.codigo:
            print(f"[ACTUALIZACIÓN] Estudiante con código {codigo} actualizado.")

    def inorden(self, nodo: Optional[NodoAVL]):
        """
        Este método será responsable de realizar un recorrido inorden del árbol AVL

        Args:
            nodo (Optional[NodoAVL]): El nodo actual en el recorrido
        """
        if nodo:
            self.inorden(nodo.izquierda)
            print(f"{nodo.estudiante.codigo} - {nodo.estudiante.nombre}")
            self.inorden(nodo.derecha)

    def buscar_por_codigo(self, codigo: int) -> Optional[Estudiante]:
        """
        Este método será responsable de buscar un estudiante por su código usando búsqueda binaria

        Args:
            codigo (int): El código del estudiante que se busca

        Returns:
            Optional[Estudiante]: El estudiante encontrado o None si no existe
        """
        nodo = self.raiz
        while nodo:
            if codigo == nodo.estudiante.codigo:
                return nodo.estudiante
            elif codigo < nodo.estudiante.codigo:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        return None

    def convertir_a_binarytree(self, nodo: Optional[NodoAVL]) -> Optional[BinaryTreeNode]:
        """
        Este método será responsable de convertir el árbol AVL a formato binarytree para visualización

        Args:
            nodo (Optional[NodoAVL]): El nodo actual que se está convirtiendo

        Returns:
            Optional[BinaryTreeNode]: El nodo convertido a formato binarytree
        """
        if not nodo:
            return None
        
        bt_node = BinaryTreeNode(nodo.estudiante.codigo)
        bt_node.left = self.convertir_a_binarytree(nodo.izquierda)
        bt_node.right = self.convertir_a_binarytree(nodo.derecha)
        
        return bt_node
    
    def mostrar_arbol_binarytree(self):
        """
        Este método será responsable de mostrar el árbol usando la librería binarytree

        """
        if not self.raiz:
            print("Árbol vacío")
            return
        
        arbol_bt = self.convertir_a_binarytree(self.raiz)
        
        print("\n[VISUALIZACIÓN DEL ÁRBOL AVL]")
        print(arbol_bt)
        
        print(f"\nAltura del árbol: {1 + arbol_bt.height}")
        print(f"Número de nodos: {arbol_bt.size}")
        print(f"Número de hojas: {arbol_bt.leaf_count}")