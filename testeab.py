from apoio.minimax_node import Node

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.isTerminal:
        return node.value
    if maximizingPlayer:
        v = -float("inf")
        for child in node.children:
            v = max(v, alphabeta(child, depth-1, alpha, beta, 0))
            alpha = max(alpha, v)
            if beta <= alpha:
                break #(* beta cut-off *)
        return v
    else:
        v = float("inf")
        for child in node.children:
            v = min(v, alphabeta(child, depth-1, alpha, beta, 1))
            beta = min(beta, v)
            if beta <= alpha:
                break #(* alpha cut-off *)
        return v

origin = Node(None, None, None)

A = Node(None, None, origin)
B = Node(None, None, origin)

D = Node(None, None, A)
E = Node(None, None, A)
F = Node(None, None, B)
G = Node(None, None, B)

J = Node(None, None, D)
K = Node(None, None, D)
L = Node(None, None, E)
M = Node(None, None, F)
N = Node(None, None, F)
O = Node(None, None, G)

S = Node(None, None, J)
T = Node(None, None, J)
U = Node(None, None, K)
Z = Node(None, None, L)
A1 = Node(None, None, M)
B1 = Node(None, None, M)
C1 = Node(None, None, N)
D1 = Node(None, None, O)
E1 = Node(None, None, O)

S.set_value(10)
T.set_value(10000000)
U.set_value(5)
Z.set_value(-10)
A1.set_value(7)
B1.set_value(5)
C1.set_value(-1000000)
D1.set_value(-7)
E1.set_value(-5)

# origin = Node(None, None, None)

# A = Node(None, None, origin)
# B = Node(None, None, origin)
# C = Node(None, None, origin)

# D = Node(None, None, A)
# E = Node(None, None, A)
# F = Node(None, None, B)
# G = Node(None, None, B)
# H = Node(None, None, C)
# I = Node(None, None, C)

# J = Node(None, None, D)
# K = Node(None, None, D)
# L = Node(None, None, E)
# M = Node(None, None, F)
# N = Node(None, None, F)
# O = Node(None, None, G)
# P = Node(None, None, H)
# Q = Node(None, None, I)
# R = Node(None, None, I)

# S = Node(None, None, J)
# T = Node(None, None, J)
# U = Node(None, None, K)
# V = Node(None, None, K)
# X = Node(None, None, K)
# Z = Node(None, None, L)
# A1 = Node(None, None, M)
# B1 = Node(None, None, N)
# C1 = Node(None, None, N)
# D1 = Node(None, None, O)
# E1 = Node(None, None, P)
# F1 = Node(None, None, Q)
# G1 = Node(None, None, Q)
# H1 = Node(None, None, R)

# S.set_value(5)
# T.set_value(6)
# U.set_value(7)
# V.set_value(4)
# X.set_value(5)
# Z.set_value(3)
# A1.set_value(6)
# B1.set_value(6)
# C1.set_value(9)
# D1.set_value(7)
# E1.set_value(5)
# F1.set_value(9)
# G1.set_value(8)
# H1.set_value(6)

print alphabeta(origin, 10, -float("inf"), float("inf"), 1)