class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        column = {}
        box = {}
        for r in range(3):
            for c in range(3):
                box[(r,c)] = set()
        for i in range(9):
            rows[i] = set()
            column[i] = set()
        for r in range(9):
            for c in range(9):

                num = board[r][c]
                if num==".":
                    continue
                box_id=(r//3,c//3)
                if num in rows[r] or num in column[c] or num in box[box_id]:
                    return False
                rows[r].add(num)
                column[c].add(num)
                box[box_id].add(num)

        return True
