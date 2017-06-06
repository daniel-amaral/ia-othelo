from models.move import Move

REGION_1 = [Move(3, 3), Move(3, 4), Move(3, 5), Move(3, 6),
            Move(4, 3), Move(4, 4), Move(4, 5), Move(4, 6),
            Move(5, 3), Move(5, 4), Move(5, 5), Move(5, 6),
            Move(6, 3), Move(6, 4), Move(6, 5), Move(6, 6)]

REGION_2 = [Move(2, 3), Move(2, 4), Move(2, 5), Move(2, 6),
            Move(3, 7), Move(4, 7), Move(5, 7), Move(6, 7),
            Move(7, 3), Move(7, 4), Move(7, 5), Move(7, 6),
            Move(3, 2), Move(4, 2), Move(5, 2), Move(6, 2)]

REGION_3 = [Move(1, 3), Move(1, 4), Move(1, 5), Move(1, 6),
            Move(3, 8), Move(4, 8), Move(5, 8), Move(6, 8),
            Move(8, 3), Move(8, 4), Move(8, 5), Move(8, 6),
            Move(3, 1), Move(4, 1), Move(5, 1), Move(6, 1)]

REGION_4 = [Move(1, 2), Move(2, 1), Move(2, 2),
            Move(1, 7), Move(2, 7), Move(2, 8),
            Move(7, 7), Move(7, 8), Move(8, 7),
            Move(7, 1), Move(7, 2), Move(8, 2)]

REGION_5 = [Move(1, 1), Move(1, 8), Move(8, 8), Move(8, 1)]


class DevPlayer:

    def __init__(self, color):
        self.color = color

    def play(self, board):
        valid_moves = board.valid_moves(self.color)
        return self.get_best_move(valid_moves)

    def get_best_move(self, valid_moves):
        # Regions priority: 5 > 3 > 1 > 2 > 4
        region_5_moves = self.intersection_of_moves_lists(REGION_5, valid_moves)
        if len(region_5_moves):
            return region_5_moves.pop()

        region_3_moves = self.intersection_of_moves_lists(REGION_3, valid_moves)
        if len(region_3_moves):
            return region_3_moves.pop()

        region_1_moves = self.intersection_of_moves_lists(REGION_1, valid_moves)
        if len(region_1_moves):
            return region_1_moves.pop()

        region_2_moves = self.intersection_of_moves_lists(REGION_2, valid_moves)
        if len(region_2_moves):
            return region_2_moves.pop()

        region_4_moves = self.intersection_of_moves_lists(REGION_4, valid_moves)
        if len(region_4_moves):
            return region_4_moves.pop()
        return None

    @staticmethod
    def intersection_of_moves_lists(desired_moves, valid_moves):
        ret = []
        for a in desired_moves:
            for b in valid_moves:
                if (a.x == b.x) and (a.y == b.y):
                    ret.append(b)
        return ret