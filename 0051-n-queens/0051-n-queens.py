class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 인덱스 : 행, 값 : 열
        # (1, 3) 위치 => visited[1] = 3
        visited = [-1] * n
        answers = []

        def is_ok_on(nth_row):
            for row in range(nth_row):
                if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                    return False
            return True

        def dfs(row):

            # 종료
            if row >= n:
                grid = [['.'] * n for _ in range(n)]
                for idx, value in enumerate(visited):
                    grid[idx][value] = 'Q'
                result = []
                for row in grid:
                    result.append(''.join(row))
                answers.append(result)
                return

            # visited[row] 의 값을 결정
            for col in range(n):
                visited[row] = col
                if is_ok_on(row):
                    dfs(row + 1)

        dfs(0)
        return answers