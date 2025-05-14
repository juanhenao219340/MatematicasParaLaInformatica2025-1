from binaryTree import BinaryTree

def main():
    tree = BinaryTree()
    tree.build_tree()

    while True:
        print("\n=== MENÚ DE OPERACIONES ===")
        print("1. Mostrar árbol")
        print("2. Graficar árbol")
        print("3. Altura del árbol")
        print("4. Recorrido inOrder")
        print("5. Recorrido preOrder")
        print("6. Recorrido postOrder")
        print("7. Todos los recorridos")
        print("8. Graficar hojas del árbol")
        print("9. Salir")

        option = input("Seleccione una opción: ")

        if option == '1':
            print("\nEstructura del árbol:")
            tree.display_tree()
        if option == '2':
            print("\nEstructura del árbol:")
            tree.draw_tree()
        elif option == '3':
            print(f"\nAltura del árbol: {tree.height()}")
        elif option == '4':
            print("\nRecorrido inOrder:")
            tree.in_order()
            print()
        elif option == '5':
            print("\nRecorrido preOrder:")
            tree.pre_order()
            print()
        elif option == '6':
            print("\nRecorrido postOrder:")
            tree.post_order()
            print()
        elif option == '7':
            tree.all_traversals()
        elif option == '8':
            tree.draw_leaves()
        elif option == '9':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
