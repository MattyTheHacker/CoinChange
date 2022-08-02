def _change_matrix(coin_set, change_amount):
    matrix = [[0 for m in range(change_amount + 1)]
              for m in range(len(coin_set) + 1)]
    for i in range(change_amount + 1):
        matrix[0][i] = i
    return matrix


def change_making(coins, change):
    matrix = _change_matrix(coins, change)

    for c in range(1, len(coins) + 1):
        for row in range(1, change + 1):
            if coins[c - 1] == row:
                matrix[c][row] = 1
            elif coins[c - 1] > row:
                matrix[c][row] = matrix[c - 1][row]
            else:
                matrix[c][row] = min(matrix[c - 1][row],
                                     1 + matrix[c][row - coins[c - 1]])
    return matrix[-1][-1]


print(change_making([1, 2, 5, 10, 20, 50, 100, 200], 32))
