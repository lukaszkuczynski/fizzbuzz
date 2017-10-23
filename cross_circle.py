
""" this is definition
1 - cross
0 - circle
"""

class CrossCircle:
    def who_won(self, scores):
        return self.diagonal(scores) or self.row(scores) or self.column(scores)

    def diagonal(self, scores):
        return None

    def row(self, scores):
        for row in scores:
            if sum(row) == 3:
                return 'cross'
            elif sum(row) == 0:
                return 'circle'

    def column(self, scores):
        columns = [
            [scores[0][0], scores[1][0], scores[2][0]],
            [scores[0][1], scores[1][1], scores[2][1]],
            [scores[0][2], scores[1][2], scores[2][2]]
        ]
        return self.row(columns)


if __name__ == '__main__':
    cc = CrossCircle()
    won = cc.who_won([[0,0,1],[0,1,1],[1,0,1]])
    print(won)
