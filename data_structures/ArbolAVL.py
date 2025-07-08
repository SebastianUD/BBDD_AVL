from typing import Optional
from models.EntidadBase import EntidadBase
from data_structures.NodoAVL import NodoAVL
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
        
        print(f"[BALANCEO] Rotación derecha en nodo {y.entidad.get_codigo()}")
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
        
        print(f"[BALANCEO] Rotación izquierda en nodo {x.entidad.get_codigo()}")
        return y

    def balancear_nodo(self, nodo: NodoAVL, codigo: int) -> NodoAVL:
        """
        Este método será responsable de balancear un nodo si es necesario después de inserción/eliminación

        Args:
            nodo (NodoAVL): El nodo que se va a balancear
            codigo (int): El código de la entidad que se insertó/eliminó para determinar el tipo de rotación

        Returns:
            NodoAVL: El nodo balanceado (puede ser el mismo nodo si no necesitaba balanceo)
        """
        balance = self.obtener_balance(nodo)
        
        if abs(balance) > 1:
            print(f"[BALANCE] Nodo {nodo.entidad.get_codigo()} tiene balance {balance}")
        
        # Caso Izquierda-Izquierda
        if balance < -1 and codigo < nodo.izquierda.entidad.get_codigo():
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Derecha
        if balance > 1 and codigo > nodo.derecha.entidad.get_codigo():
            return self.rotacion_izquierda(nodo)
        
        # Caso Izquierda-Derecha
        if balance < -1 and codigo > nodo.izquierda.entidad.get_codigo():
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Izquierda
        if balance > 1 and codigo < nodo.derecha.entidad.get_codigo():
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)
        
        return nodo

    def insertar(self, nodo: Optional[NodoAVL], entidad: EntidadBase, mostrar_mensajes: bool = True) -> NodoAVL:
        """
        Este método será responsable de insertar una nueva entidad en el árbol AVL

        Args:
            nodo (Optional[NodoAVL]): El nodo actual donde se intenta insertar
            entidad (EntidadBase): La entidad que se va a insertar
            mostrar_mensajes (bool): Si se deben mostrar mensajes de debug durante la inserción

        Returns:
            NodoAVL: El nodo raíz del subárbol después de la inserción y balanceo
        """
        if not nodo:
            if mostrar_mensajes:
                print(f"[INSERCIÓN] Nuevo nodo creado con código {entidad.get_codigo()}")
            return NodoAVL(entidad)

        if entidad.get_codigo() < nodo.entidad.get_codigo():
            nodo.izquierda = self.insertar(nodo.izquierda, entidad, mostrar_mensajes)
        elif entidad.get_codigo() > nodo.entidad.get_codigo():
            nodo.derecha = self.insertar(nodo.derecha, entidad, mostrar_mensajes)
        else:
            if mostrar_mensajes:
                print(f"[ADVERTENCIA] Código {entidad.get_codigo()} ya existe. No se insertó.")
            return nodo

        # Actualizar altura y balancear
        self.actualizar_altura(nodo)
        return self.balancear_nodo(nodo, entidad.get_codigo())

    def obtener_maximo_valor_nodo(self, nodo: NodoAVL) -> NodoAVL:
        """
        Este método encontrará el nodo con el valor máximo en el subárbol izquierdo

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
        Este método será responsable de eliminar una entidad del árbol AVL

        Args:
            nodo (Optional[NodoAVL]): El nodo actual donde se busca la entidad a eliminar
            codigo (int): El código de la entidad que se va a eliminar

        Returns:
            Optional[NodoAVL]: El nodo raíz del subárbol después de la eliminación y balanceo
        """
        if not nodo:
            print(f"[ADVERTENCIA] Código {codigo} no encontrado para eliminar.")
            return nodo

        # Búsqueda del nodo a eliminar
        if codigo < nodo.entidad.get_codigo():
            nodo.izquierda = self.eliminar(nodo.izquierda, codigo)
        elif codigo > nodo.entidad.get_codigo():
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
            nodo.entidad = temp.entidad
            nodo.izquierda = self.eliminar(nodo.izquierda, temp.entidad.get_codigo())

        # Actualizar altura
        self.actualizar_altura(nodo)
        
        # Balancear el árbol
        balance = self.obtener_balance(nodo)
        
        if abs(balance) > 1:
            print(f"[BALANCE] Nodo {nodo.entidad.get_codigo()} tiene balance {balance}")

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

    def agregar_entidad(self, entidad: EntidadBase):
        """
        Este método será responsable de agregar una entidad al árbol AVL

        Args:
            entidad (EntidadBase): La entidad que se va a agregar al árbol
        """
        print(f"\n[OPERACIÓN] Insertando entidad con código {entidad.get_codigo()}")
        self.raiz = self.insertar(self.raiz, entidad)

    def eliminar_entidad(self, codigo: int):
        """
        Este método será responsable de eliminar una entidad del árbol AVL

        Args:
            codigo (int): El código de la entidad que se va a eliminar
        """
        print(f"\n[OPERACIÓN] Eliminando entidad con código {codigo}")
        self.raiz = self.eliminar(self.raiz, codigo)

    def actualizar_entidad(self, codigo: int, nueva_entidad: EntidadBase):
        """
        Este método será responsable de actualizar los datos de una entidad existente sin modificar la estructura del árbol

        Args:
            codigo (int): El código de la entidad que se va a actualizar
            nueva_entidad (EntidadBase): Los nuevos datos de la entidad
        """
        print(f"\n[OPERACIÓN] Actualizando entidad con código {codigo}")
        
        # Buscar el nodo a actualizar
        nodo = self._buscar_nodo(self.raiz, codigo)
        if nodo:
            # Actualizar solo los datos del nodo, manteniendo la estructura del árbol
            nodo.entidad = nueva_entidad
            print(f"[ACTUALIZACIÓN] Entidad con código {codigo} actualizada correctamente.")
        else:
            print(f"[ERROR] No se encontró entidad con código {codigo} para actualizar.")
    
    def _buscar_nodo(self, nodo: Optional[NodoAVL], codigo: int) -> Optional[NodoAVL]:
        """
        Método privado para buscar un nodo específico por código

        Args:
            nodo (Optional[NodoAVL]): El nodo actual en la búsqueda
            codigo (int): El código que se está buscando

        Returns:
            Optional[NodoAVL]: El nodo encontrado o None si no existe
        """
        if not nodo:
            return None
        
        if codigo == nodo.entidad.get_codigo():
            return nodo
        elif codigo < nodo.entidad.get_codigo():
            return self._buscar_nodo(nodo.izquierda, codigo)
        else:
            return self._buscar_nodo(nodo.derecha, codigo)

    def inorden(self, nodo: Optional[NodoAVL]):
        """
        Este método será responsable de realizar un recorrido inorden del árbol AVL

        Args:
            nodo (Optional[NodoAVL]): El nodo actual en el recorrido
        """
        if nodo:
            self.inorden(nodo.izquierda)
            print(f"{nodo.entidad}")
            self.inorden(nodo.derecha)

    def inorden_lista(self) -> list:
        """
        Devuelve una lista de entidades en orden ascendente por su código. Este método es útil para usarlo en la interfaz gráfica.
        """
        resultado = []
        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierda)
                resultado.append(nodo.entidad)
                recorrer(nodo.derecha)
        recorrer(self.raiz)
        return resultado

    def buscar_por_codigo(self, codigo: int) -> Optional[EntidadBase]:
        """
        Este método será responsable de buscar una entidad por su código usando búsqueda binaria

        Args:
            codigo (int): El código de la entidad que se busca

        Returns:
            Optional[EntidadBase]: La entidad encontrada o None si no existe
        """
        nodo = self.raiz
        while nodo:
            if codigo == nodo.entidad.get_codigo():
                return nodo.entidad
            elif codigo < nodo.entidad.get_codigo():
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
        
        bt_node = BinaryTreeNode(nodo.entidad.get_codigo())
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