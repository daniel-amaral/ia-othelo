from apoio.minimax_node import Node
from apoio.minimax_tree import Tree
from apoio.regions import Regions
from models.move import Move

MAX_DEPTH = 5
REGIONS = Regions()
NEXT_NODE = None


class ObjetivePlayer:

    def __init__(self, color):
        self.color = color

    def play(self, board):
        valid_moves = self.remove_duplicated_moves(board.valid_moves(self.color))
        if len(valid_moves) is 1:
            return valid_moves[0]

        root_node = Node(None, board, None)
        value = self.alphabeta(root_node, MAX_DEPTH, -float("inf"), float("inf"), 1, board, self.color)
         
        next_childs = root_node.get_childs_with_value(value)
        next_moves = []
        for x in next_childs:
            next_moves.append(x.move)
        
        next_move = self.__slice_best_moves_in_list(next_moves)

        if len(next_move) > 0:
            next_move = next_move[0]
            if isinstance(next_move, Move):
                return next_move

        return valid_moves[0]

    def remove_duplicated_moves(self, valid_moves):
        optimized_valid_moves = []

        for valid_move in valid_moves:
            isInside = False
            for optimized_valid_move in optimized_valid_moves:
                if valid_move.x == optimized_valid_move.x and valid_move.y == optimized_valid_move.y:
                    isInside = True
                    break
            if isInside:
                continue
            optimized_valid_moves.append(valid_move)

        return optimized_valid_moves

    def alphabeta(self, node, depth, alpha, beta, maximizingPlayer, board, color):
        if depth == 0: # or node.isTerminal: TODO: Pensar sobre a necessidade disso depois
            # if maximizingPlayer:
            score = self.calculate_score_diff(board)
            node.set_value(score)
            return score
        if maximizingPlayer:
            v = float("-inf")
            valid_moves = self.remove_duplicated_moves(board.valid_moves(color))
            valid_moves = self.__slice_best_moves_in_list(valid_moves)
            if len(valid_moves) is 0:
                score = self.calculate_score_diff(board)
                node.set_value(score)
                return score
            for move in valid_moves:
                new_board = board.get_clone()
                new_board.play(move, color)
                child = Node(move, new_board, node)
            # for child in node.children:
                v = max(v, self.alphabeta(child, depth-1, alpha, beta, 0, new_board, self._opponent(color)))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break #(* beta cut-off *)
            node.set_value(v)
            return v
        else:
            v = float("inf")
            valid_moves = self.remove_duplicated_moves(board.valid_moves(color))
            if len(valid_moves) is 0:
                score = self.calculate_score_diff(board)
                node.set_value(score)
                return score
            for move in valid_moves:
                new_board = board.get_clone()
                new_board.play(move, color)
                child = Node(move, new_board, node)
            # for child in node.children:
                v = min(v, self.alphabeta(child, depth-1, alpha, beta, 1, new_board, self.color))
                beta = min(beta, v)
                if beta <= alpha:
                    break #(* alpha cut-off *)
            node.set_value(v)
            return v

    def calculate_score_diff(self, board):
        board_score = board.score()
        white_score = board_score[0]
        black_score = board_score[1]
        if self.color is 'o':   # white
            return white_score - black_score
        return black_score - white_score

    def __slice_best_moves_in_list(self, moves):
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

    def _opponent(self, color):
        return '@' if color is 'o' else 'o'