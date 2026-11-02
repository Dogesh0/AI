N = int(input("Enter total number of Queen : "))

def isSafe(board, row, col):

    for i in range(N):
        if board[row][i] == 1:
            return False

    for i in range(N):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row):

    if row == N:
        return True

    for col in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1

            if solve(board, row + 1):
                return True

            board[row][col] = 0

    return False


def main():
    board = [[0] * N for i in range(N)]

    if solve(board, 0):
        print("Solution:")

        for i in range(N):
            for j in range(N):
                print(board[i][j], end=" ")
            print()
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()


"""
def solve(board):

    next_col = [0] * N
    row = 0

    while row < N:

        col = next_col[row]

        while col < N and not isSafe(board, row, col):
            col += 1

        if col < N:
            board[row][col] = 1
            next_col[row] = col + 1

            row += 1

            if row < N:
                next_col[row] = 0

        else:
            next_col[row] = 0
            row -= 1
          
            if row >= 0:
                col = next_col[row] - 1
                board[row][col] = 0

    return row == N

"""