from node import Node
import networkx as nx
import matplotlib.pyplot as plt

class BinaryTree:
    def __init__(self):
        self.nodes = {}  # diccionario para mapear valor -> Node
        self.root = None

    def build_tree(self):
        print("\n=== FASE 1: INGRESO DE NODOS ===")
        while True:
            try:
                value = int(input("Ingrese el valor del nodo (0 para terminar): "))
                if value == 0:
                    break
                if value in self.nodes:
                    print("Este valor ya existe. Intente con otro.")
                    continue
                node = Node(value)
                self.nodes[value] = node
            except ValueError:
                print("Valor inválido. Ingrese un entero positivo.")

        print("\n=== FASE 2: DEFINICIÓN DE RELACIONES ===")
        for val, node in self.nodes.items():
            while True:
                try:
                    l_val = int(input(f"Ingrese el valor del hijo izquierdo de {val} (0 si no tiene): "))
                    if l_val == val:
                        print("Un nodo no puede ser hijo de sí mismo.")
                        continue
                    if l_val != 0 and l_val not in self.nodes:
                        print("Ese nodo no fue ingresado. Intente nuevamente.")
                        continue
                    if l_val != 0:
                        node.set_left(self.nodes[l_val])
                    break
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")

            while True:
                try:
                    r_val = int(input(f"Ingrese el valor del hijo derecho de {val} (0 si no tiene): "))
                    if r_val == val:
                        print("Un nodo no puede ser hijo de sí mismo.")
                        continue
                    if r_val != 0 and r_val not in self.nodes:
                        print("Ese nodo no fue ingresado. Intente nuevamente.")
                        continue
                    if r_val != 0:
                        node.set_right(self.nodes[r_val])
                    break
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")

        while True:
            try:
                root_val = int(input("\nIngrese el valor del nodo raíz: "))
                if root_val in self.nodes:
                    self.root = self.nodes[root_val]
                    break
                else:
                    print("Ese nodo no fue ingresado.")
            except ValueError:
                print("Valor inválido.")

    def display_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.get_right():
            self.display_tree(node.get_right(), level + 1)
        print('    ' * level + f'[{node.get_value()}]')
        if node.get_left():
            self.display_tree(node.get_left(), level + 1)

    def draw_tree(self):
        if self.root is None:
            print("El árbol está vacío.")
            return

        G = nx.DiGraph()
        pos = {}

        def add_edges(node, parent=None, x=0, y=0, dx=1.0):
            if node is None:
                return
            G.add_node(node.get_value())
            pos[node.get_value()] = (x, y)
            if parent:
                G.add_edge(parent.get_value(), node.get_value())
            # Izquierda ↓
            add_edges(node.get_left(), node, x - dx, y - 1, dx / 2)
            # Derecha ↓
            add_edges(node.get_right(), node, x + dx, y - 1, dx / 2)

        add_edges(self.root)

        plt.figure(figsize=(10, 6))
        nx.draw(
            G,
            pos=pos,
            with_labels=True,
            arrows=True,
            node_color="lightgreen",
            node_size=1500,
            font_size=12,
            font_weight='bold'
        )
        plt.title("Árbol Binario")
        plt.gca().invert_yaxis()  # Coloca la raíz arriba
        plt.show()

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_h = self.height(node.get_left()) if node.get_left() else 0
        right_h = self.height(node.get_right()) if node.get_right() else 0
        return 1 + max(left_h, right_h)

    def in_order(self, node=None):
        if node is None:
            node = self.root
        if node.get_left():
            self.in_order(node.get_left())
        print(node.get_value(), end=' ')
        if node.get_right():
            self.in_order(node.get_right())

    def pre_order(self, node=None):
        if node is None:
            node = self.root
        print(node.get_value(), end=' ')
        if node.get_left():
            self.pre_order(node.get_left())
        if node.get_right():
            self.pre_order(node.get_right())

    def post_order(self, node=None):
        if node is None:
            node = self.root
        if node.get_left():
            self.post_order(node.get_left())
        if node.get_right():
            self.post_order(node.get_right())
        print(node.get_value(), end=' ')

    def all_traversals(self):
        print("\nRecorrido inOrder:")
        self.in_order()
        print("\nRecorrido preOrder:")
        self.pre_order()
        print("\nRecorrido postOrder:")
        self.post_order()
        print()

    def draw_leaves(self):
        if not self.nodes:
            print("El árbol está vacío.")
            return

        # Buscar nodos sin hijos
        candidates = [node for node in self.nodes.values()
                    if node.get_left() is None and node.get_right() is None]

        # Ahora filtramos los que tampoco son hijos de nadie
        children_ids = set()
        for node in self.nodes.values():
            if node.get_left():
                children_ids.add(node.get_left().get_value())
            if node.get_right():
                children_ids.add(node.get_right().get_value())

        # Aislados: sin hijos ni padre
        isolated_nodes = [node for node in candidates
                        if node.get_value() not in children_ids]

        if not isolated_nodes:
            print("No hay nodos completamente aislados (sin padre ni hijos).")
            return

        # Graficar nodos aislados
        G = nx.Graph()
        pos = {}
        for idx, node in enumerate(isolated_nodes):
            G.add_node(node.get_value())
            pos[node.get_value()] = (idx, 0)

        plt.figure(figsize=(10, 2))
        nx.draw(
            G,
            pos=pos,
            with_labels=True,
            node_color="orange",
            node_size=1000,
            font_size=12,
            font_weight='bold'
        )
        plt.title("Nodos aislados (sin padre ni hijos)")
        plt.show()

