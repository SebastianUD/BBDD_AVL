from typing import Optional
from Estudiante import Estudiante
from NodoAVL import NodoAVL
from binarytree import Node as BinaryTreeNode


# Árbol AVL completo con todas las operaciones
class ArbolAVL:
    def __init__(self):
        self.raiz: Optional[NodoAVL] = None

    def obtener_altura(self, nodo: Optional[NodoAVL]) -> int:
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo: Optional[NodoAVL]) -> int:
        return self.obtener_altura(nodo.derecha) - self.obtener_altura(nodo.izquierda) if nodo else 0

    def actualizar_altura(self, nodo: NodoAVL):
        """Actualiza la altura de un nodo basándose en sus hijos"""
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

    def rotacion_derecha(self, y: NodoAVL) -> NodoAVL:
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
        """Balancea un nodo si es necesario después de inserción/eliminación"""
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
        """Encuentra el nodo con el valor máximo en el subárbol"""
        while nodo.derecha:
            nodo = nodo.derecha
        return nodo

    def eliminar(self, nodo: Optional[NodoAVL], codigo: int) -> Optional[NodoAVL]:
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
        print(f"\n[OPERACIÓN] Insertando estudiante con código {estudiante.codigo}")
        self.raiz = self.insertar(self.raiz, estudiante)

    def eliminar_estudiante(self, codigo: int):
        print(f"\n[OPERACIÓN] Eliminando estudiante con código {codigo}")
        self.raiz = self.eliminar(self.raiz, codigo)

    def actualizar_estudiante(self, codigo: int, nuevo_estudiante: Estudiante):
        """Actualiza un estudiante eliminando el antiguo e insertando el nuevo"""
        print(f"\n[OPERACIÓN] Actualizando estudiante con código {codigo}")
        self.raiz = self.eliminar(self.raiz, codigo)
        self.raiz = self.insertar(self.raiz, nuevo_estudiante)
        if codigo == nuevo_estudiante.codigo:
            print(f"[ACTUALIZACIÓN] Estudiante con código {codigo} actualizado.")

    def inorden(self, nodo: Optional[NodoAVL]):
        if nodo:
            self.inorden(nodo.izquierda)
            print(f"{nodo.estudiante.codigo} - {nodo.estudiante.nombre}")
            self.inorden(nodo.derecha)

    def buscar_por_codigo(self, codigo: int) -> Optional[Estudiante]:
        """Búsqueda binaria en el árbol AVL"""
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
        """Convierte el árbol AVL a formato binarytree para visualización"""
        if not nodo:
            return None
        
        bt_node = BinaryTreeNode(nodo.estudiante.codigo)
        bt_node.left = self.convertir_a_binarytree(nodo.izquierda)
        bt_node.right = self.convertir_a_binarytree(nodo.derecha)
        
        return bt_node
    
    def mostrar_arbol_binarytree(self):
        """Muestra el árbol usando la librería binarytree"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        arbol_bt = self.convertir_a_binarytree(self.raiz)
        
        print("\n[VISUALIZACIÓN DEL ÁRBOL AVL]")
        print(arbol_bt)
        
        print(f"\nAltura del árbol: {1 + arbol_bt.height}")
        print(f"Número de nodos: {arbol_bt.size}")
        print(f"Número de hojas: {arbol_bt.leaf_count}")