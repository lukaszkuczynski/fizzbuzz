
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
        return None

    def column(self, scores):
        return None


if __name__ == '__main__':
    cc = CrossCircle()
    won = cc.who_won([[0,0,1],[0,1,1],[1,0,1]])
    print(won)
