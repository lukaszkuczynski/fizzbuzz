
""" this is definition
1 - cross
0 - circle
"""

class CrossCircle:

    def who_won(self, scores):
        return \
            self.diagonal(scores) \
            or self.row(scores) \
            or self.column(scores)

    def diagonal(self, scores):
        one_diag = scores[0][0] + scores[1][1] + scores[2][2]
        other_diag = scores[0][2] + scores[1][1] + scores[2][0]
        if one_diag == 0 or other_diag == 0: return 'circle'
        elif one_diag == 3 or other_diag == 3: return 'cross'

    def row(self, scores):
        for row in scores:
            if sum(row) == 3:
                return 'cross'
            elif sum(row) == 0:
                return 'circle'

    def column(self, scores):
        transposed = [list(x) for x in zip(*scores)]
        # # todo rethink numpy or zip to transpose matrix
        # columns = [
        #     [scores[0][0], scores[1][0], scores[2][0]],
        #     [scores[0][1], scores[1][1], scores[2][1]],
        #     [scores[0][2], scores[1][2], scores[2][2]]
        # ]
        return self.row(transposed)


if __name__ == '__main__':
    cc = CrossCircle()
    # won = cc.who_won([[0,0,1],[0,1,1],[1,0,1]])
    won = cc.who_won([[0, 1, 1], [0, 0, 1], [0, 0, 1]])
    print(won)
