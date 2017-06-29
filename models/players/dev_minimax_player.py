from apoio.minimax_node import Node
from apoio.minimax_tree import Tree
from apoio.regions import Regions

MAX_DEPTH = 7
REGIONS = Regions()
NEXT_NODE = None


class MinimaxPlayer:

    def __init__(self, color):
        self.color = color

    def play(self, board):
        root_node = Node(None, board, None)
        valid_moves = list(set(board.valid_moves(self.color)))
        print '#valid moves: ' + str(len(valid_moves))
        minimax_tree = self.build_minimax_tree(root_node, board)
        tree_depth = minimax_tree.depth
        print 'tree depth: ' + str(tree_depth)
        minimax_value = self.minimax(root_node, tree_depth, True)
        next_move = root_node.get_child_with_value(minimax_value)
        # print 'minimax value: ' + str(minimax)
        return next_move.move
        if isinstance(minimax, Node):
            return minimax.move
        return valid_moves[0]
        # return self.get_best_move(valid_moves)

    def calculate_score_diff(self, board):
        board_score = board.score()
        white_score = board_score[0]
        black_score = board_score[1]
        if self.color is 'o':   # white
            return white_score - black_score
        return black_score - white_score

    @staticmethod
    def get_best_move(valid_moves):
        return valid_moves[0]

    def build_minimax_tree(self, root, board):
        self._recursive_create_tree(root, board, self.color, 1)
        return Tree(root)

    def _recursive_create_tree(self, node, board, color, depth):
        if depth > MAX_DEPTH:
            return
        local_depth = depth + 1
        valid_moves = board.valid_moves(color)
        if len(valid_moves) is 0:
            print 'terminal found on depth: ' + str(depth)
        best_moves = self.__slice_best_moves_in_list(valid_moves)
        for move in best_moves:
            new_board = board.get_clone()
            new_board.play(move, color)
            child_node = Node(move, new_board, node)
            # node.add_child(child_node)
            self._recursive_create_tree(child_node, new_board, self._opponent(color), local_depth)

    @staticmethod
    def __slice_best_moves_in_list(moves):
        # Regions priority: 5 > 3 > 1 > 2 > 4
        prioritized_regions = [
            REGIONS.get_region(5),
            REGIONS.get_region(3),
            REGIONS.get_region(1),
            REGIONS.get_region(2),
            REGIONS.get_region(4),
        ]
        for region_movies in prioritized_regions:
            match_moves = REGIONS.intersection_of_moves_lists(region_movies, moves)
            if len(match_moves) > 0:
                return match_moves
        return []

    @staticmethod
    def minimax(node, depth, isMax):
        if depth is 0:
            return 0
        if node.isTerminal:
            if node.move is None:
                return 0
            return REGIONS.get_move_value(node.move)
        if isMax:
            best_value = -float('inf')
            NEXT_NODE = node.children[0]
            for child in node.children:
                value = MinimaxPlayer.minimax(child, depth-1, False)
                # if value > best_value:
                #     NEXT_NODE = child
                best_value = max(best_value, value)
                child.set_value(best_value)
            # if depth is MAX_DEPTH+1:
            #     return NEXT_NODE
                return best_value
        else:   # isMin
            best_value = float('inf')
            for child in node.children:
                value = MinimaxPlayer.minimax(child, depth-1, True)
                best_value = min(best_value, value)
                child.set_value(best_value)
                return best_value

    @staticmethod
    def remove_duplicated_moves(list_of_moves):
        return None

    @staticmethod
    def _opponent(color):
        return '@' if color is 'o' else 'o'
