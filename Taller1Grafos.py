def get_vertices():
    while True:
        vertices = input("Ingrese los nombres de los vértices separados por comas (Ejemplo: A,B,C): ").replace(" ", "").split(",")
        if all(len(v) == 1 for v in vertices):
            return vertices
        print("Error: Los vértices deben ser un solo carácter cada uno.")


def get_adjacency_matrix(vertices):
    n = len(vertices)
    matrix = []
    print("Ingrese la matriz de adyacencia fila por fila, separando los valores con espacios (Ejemplo: 0 0 0 0):")
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Fila {i+1} ({vertices[i]}): ").split()))
                if len(row) == n and all(x in [0, 1] for x in row):
                    matrix.append(row)
                    break
                print("Error: La fila debe contener exactamente", n, "valores 0 o 1.")
            except ValueError:
                print("Error: Ingrese solo números 0 o 1.")
    return matrix


def validate_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def matrix_to_edges(matrix, vertices):
    edges = set()
    n = len(vertices)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                edges.add((vertices[i], vertices[j]))
    return edges


def get_edges():
    while True:
        try:
            edges_input = input("Ingrese las aristas en formato (A,B) separadas por punto y comas (Ejemplo: (A,B);(B,C)): ").replace(" ", "")
            edges = set()
            for pair in edges_input.split(";"):
                print(pair)
                if pair.startswith("(") and pair.endswith(")"):
                    a, b = pair[1:-1].split(",")
                    if len(a) == 1 and len(b) == 1:
                        edges.add((a, b))
                    else:
                        raise ValueError
                else:
                    raise ValueError
            return edges
        except ValueError:
            print("Error: Ingrese aristas en el formato correcto.")


def edges_to_matrix(vertices, edges):
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]
    vertex_index = {v: i for i, v in enumerate(vertices)}
    for a, b in edges:
        if a in vertex_index and b in vertex_index:
            i, j = vertex_index[a], vertex_index[b]
            matrix[i][j] = matrix[j][i] = 1
    return matrix


def print_matrix(matrix, vertices):
    print("\nMatriz de adyacencia:")
    print("  ", " ".join(vertices))
    for i, row in enumerate(matrix):
        print(vertices[i], " ", " ".join(map(str, row)))


def main():
    while True:
        print("\nMenú:")
        print("1. Ingresar matriz de adyacencia")
        print("2. Ingresar vértices y aristas")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            vertices = get_vertices()
            matrix = get_adjacency_matrix(vertices)
            if validate_symmetric(matrix):
                edges = matrix_to_edges(matrix, vertices)
                print("\nVértices:", vertices)
                print("Aristas:", edges)
            else:
                print("Error: La matriz no es simétrica. No es un grafo válido.")

        elif choice == "2":
            vertices = get_vertices()
            edges = get_edges()
            matrix = edges_to_matrix(vertices, edges)
            print_matrix(matrix, vertices)

        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


main()
