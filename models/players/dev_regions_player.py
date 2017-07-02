from apoio.regions import Regions

regions = Regions()


class RegionsPlayer:

    def __init__(self, color):
        self.color = color

    def play(self, board):
        valid_moves = self.optimizeValidMoves(board.valid_moves(self.color))
        return self.get_best_move(valid_moves)

    def optimizeValidMoves(self, valid_moves):
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

    def get_best_move(self, valid_moves):
        # Regions priority: 5 > 3 > 1 > 2 > 4
        prioritized_regions = [
            regions.get_region(5),
            regions.get_region(3),
            regions.get_region(1),
            regions.get_region(2),
            regions.get_region(4),
        ]
        for region in prioritized_regions:
            region_moves = regions.intersection_of_moves_lists(region, valid_moves)
            if len(region_moves):
                return region_moves.pop()
        return None

