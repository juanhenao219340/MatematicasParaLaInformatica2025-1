class Node:
    __value = None
    __left = None
    __right = None

    def __init__(self, value):
        self.set_value(value)

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if isinstance(value, int) and value > 0:
            self.__value = value
        else:
            raise ValueError("El valor debe ser un número entero positivo.")

    def get_left(self):
        return self.__left

    def set_left(self, node):
        if node is None or isinstance(node, Node):
            self.__left = node
        else:
            raise TypeError("El hijo izquierdo debe ser un objeto de tipo Node o None.")

    def get_right(self):
        return self.__right

    def set_right(self, node):
        if node is None or isinstance(node, Node):
            self.__right = node
        else:
            raise TypeError("El hijo derecho debe ser un objeto de tipo Node.")