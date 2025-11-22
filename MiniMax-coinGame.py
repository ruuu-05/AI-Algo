coins = [8, 15, 3, 7]

# P1 -> MAX , P2 -> MIN
def miniMax(L, R, turn1):
    if L > R:
        return 0

    if turn1:  # P1's turn
        left = coins[L] + miniMax(L + 1, R, False)
        right = coins[R] + miniMax(L, R - 1, False)
        return max(left, right)
    else:  # P2's turn
        left = miniMax(L + 1, R, True)
        right = miniMax(L, R - 1, True)
        return min(left, right)

# P1 chooses best move (maximize)
def best_p1(L, R):
    takeLeft = coins[L] + miniMax(L + 1, R, False)
    takeRight = coins[R] + miniMax(L, R - 1, False)
    if takeLeft >= takeRight:
        return 'L', takeLeft
    else:
        return 'R', takeRight

# P2 chooses best move (minimize)
def best_p2(L, R):
    takeLeft = miniMax(L + 1, R, True)
    takeRight = miniMax(L, R - 1, True)
    if takeLeft <= takeRight:
        return 'L', takeLeft
    else:
        return 'R', takeRight

# Main game loop
p1turn = True
l, r = 0, len(coins) - 1
p1s, p2s = 0, 0

while l <= r:
    print("Coins:", coins[l:r+1])

    if p1turn:
        move, _ = best_p1(l, r)
        print(f"Player 1 picks {move}")
        if move == 'L':
            p1s += coins[l]
            l += 1
        else:
            p1s += coins[r]
            r -= 1
    else:
        move, _ = best_p2(l, r)
        print(f"Player 2 picks {move}")
        if move == 'L':
            p2s += coins[l]
            l += 1
        else:
            p2s += coins[r]
            r -= 1

    print(f"Scores -> P1: {p1s} | P2: {p2s}\n")
    p1turn = not p1turn

print("------------ GAME OVER ------------")
print(f"Final Scores -> P1: {p1s} | P2: {p2s}")
if p1s > p2s:
    print("P1 WINS!")
elif p1s < p2s:
    print("P2 WINS!")
else:
    print("DRAW!")
