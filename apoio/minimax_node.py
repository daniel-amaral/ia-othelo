

class Node:

    def __init__(self, move, board, parent=None):
        self.__move = move
        self.__board = board
        self.__children = []
        self.__parent = parent
        if parent is not None:
            parent.add_child(self)
        self.__value = None

    @property
    def move(self):
        return self.__move

    @property
    def board(self):
        return self.__board

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    @property
    def isTerminal(self):
        return len(self.__children) == 0

    @property
    def value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def set_parent(self, node):
        self.__parent = node

    def add_child(self, node):
        self.__children.append(node)
        node.set_parent(self)
        return node

    def get_child_with_value(self, value):
        for child in self.children:
            if child.value is not None:
                if child.value is value:
                    return child
        return None