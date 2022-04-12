class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def is_on_board(i, j):
            return (0 <= i < m) and (0 <= j < n)
        
        def live_dead_neighbours(i, j):
            live, dead = 0, 0
            for k in range(-1, 2):
                for p in range(-1, 2):
                    if not(k == 0 and p == 0) and is_on_board(i+k, j+p):
                        if board[i+k][j+p] == 1:
                            live += 1
                        else:
                            dead += 1
            return live, dead
        updates = []
        for i in range(m):
            for j in range(n):
                live, dead = live_dead_neighbours(i, j)
                if board [i][j] == 1:
                    if live < 2 or live > 3:
                        updates.append((i, j, 0))
                elif live == 3:
                    updates.append((i, j, 1))
                    
        for i, j, val in updates:
            board[i][j] = val
        