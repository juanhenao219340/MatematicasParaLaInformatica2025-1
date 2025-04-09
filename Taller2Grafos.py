import networkx as nx
import matplotlib.pyplot as plt

def get_vertices():
    while True:
        vertices = input("Ingrese los vértices separados por comas (Ej: A,B,C): ").replace(" ", "").split(",")
        if all(len(v) == 1 for v in vertices):
            return vertices
        print("Error: Todos los vértices deben ser un solo carácter.")

def get_adjacency_matrix(vertices):
    n = len(vertices)
    matrix = []
    print("Ingrese la matriz de adyacencia (solo 0 y 1):")
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Fila {i+1} ({vertices[i]}): ").split()))
                if len(row) == n and all(x in [0, 1] for x in row):
                    matrix.append(row)
                    break
                print("Error: La fila debe tener exactamente", n, "valores 0 o 1.")
            except ValueError:
                print("Error: Solo se permiten números 0 o 1.")
    return matrix

def validate_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def get_incidence_matrix(vertices):
    m = int(input("¿Cuántas aristas tiene el grafo?: "))
    n = len(vertices)
    matrix = []
    print("Ingrese la matriz de incidencia (valores 0 o 1, cada columna debe tener exactamente dos 1):")
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Fila {i+1} ({vertices[i]}): ").split()))
                print(f"{row}, {len(row)}, {m}")
                if len(row) == m:
                    matrix.append(row)
                    break
                print(f"Error: La fila debe contener exactamente {m} valores.")
            except ValueError:
                print("Error: Solo se permiten números.")
    # Validación por columnas
    for col in zip(*matrix):
        if col.count(1) != 2:
            print("Error: Cada columna debe tener exactamente dos valores iguales a 1.")
            return None
    return matrix

def get_edges():
    while True:
        try:
            entrada = input("Ingrese las aristas en formato (A,B);(B,C): ").replace(" ", "")
            edges = set()
            for par in entrada.split(";"):
                if par.startswith("(") and par.endswith(")"):
                    a, b = par[1:-1].split(",")
                    if len(a) == 1 and len(b) == 1:
                        edges.add((a, b))
                    else:
                        raise ValueError
                else:
                    raise ValueError
            return edges
        except ValueError:
            print("Error: Formato incorrecto. Use (A,B);(C,D)...")

def edges_to_adjacency_matrix(vertices, edges):
    n = len(vertices)
    matrix = [[0]*n for _ in range(n)]
    idx = {v: i for i, v in enumerate(vertices)}
    for a, b in edges:
        if a in idx and b in idx:
            i, j = idx[a], idx[b]
            matrix[i][j] = matrix[j][i] = 1
    return matrix

def edges_to_incidence_matrix(vertices, edges):
    n = len(vertices)
    m = len(edges)
    matrix = [[0]*m for _ in range(n)]
    idx = {v: i for i, v in enumerate(vertices)}
    for k, (a, b) in enumerate(edges):
        if a in idx and b in idx:
            i, j = idx[a], idx[b]
            matrix[i][k] = matrix[j][k] = 1
    return matrix

def print_matrix(matrix, header):
    print("  ", " ".join([str(i+1) for i in range(len(matrix[0]))]))
    for i, row in enumerate(matrix):
        print(header[i], " ", " ".join(map(str, row)))

def draw_graph(vertices, edges):
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

def main():
    while True:
        print("\nMenú:")
        print("1. Ingresar matriz de adyacencia")
        print("2. Ingresar matriz de incidencia")
        print("3. Ingresar vértices y aristas")
        print("4. Salir")
        op = input("Seleccione una opción: ")

        if op == "1":
            vertices = get_vertices()
            matrix = get_adjacency_matrix(vertices)
            if not validate_symmetric(matrix):
                print("Error: La matriz no es simétrica. No es un grafo no dirigido.")
                continue
            edges = set()
            n = len(vertices)
            for i in range(n):
                for j in range(i+1, n):
                    if matrix[i][j] == 1:
                        edges.add((vertices[i], vertices[j]))
            print("\nGrafo generado:")
            draw_graph(vertices, edges)

        elif op == "2":
            vertices = get_vertices()
            matrix = get_incidence_matrix(vertices)
            if matrix:
                edges = set()
                cols = list(zip(*matrix))
                for col in cols:
                    v = [vertices[i] for i, val in enumerate(col) if val == 1]
                    if len(v) == 2:
                        edges.add((v[0], v[1]))
                print("\nGrafo generado:")
                draw_graph(vertices, edges)

        elif op == "3":
            vertices = get_vertices()
            edges = get_edges()
            adj = edges_to_adjacency_matrix(vertices, edges)
            inc = edges_to_incidence_matrix(vertices, edges)
            print("\nMatriz de adyacencia:")
            print_matrix(adj, vertices)
            print("\nMatriz de incidencia:")
            print_matrix(inc, vertices)
            draw_graph(vertices, edges)

        elif op == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

main()