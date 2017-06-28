from minimax_node import Node


class Tree():

    def __init__(self, node=None):
        self.__root = node

    @property
    def root(self):
        return self.__root

    @property
    def depth(self):
        return self.__recursive_depth(self.root)

    @staticmethod
    def __recursive_depth(node):
        if node is None:
            return 0
        children = node.children
        max_depth = 0
        for child in children:
            max_depth = max(max_depth, Tree.__recursive_depth(child))
        return max_depth + 1

    def set_root(self, node):
        self.__root = node