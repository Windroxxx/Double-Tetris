from objects import Shape
from random import randint, choice


def make_radius(field):
    radius = field.copy()
    cl = 1
    cnt = 0
    colors = {}
    while 0 in [radius[i][j] for i in range(len(field)) for j in range(len(field[i]))]:
        for i in range(len(field)):
            for j in range(len(field[0])):
                if radius[i][j] != 0:
                    continue
                if i > 0 and radius[i - 1][j] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
                elif i > 0 and j > 0 and radius[i - 1][j - 1] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
                elif j > 0 and radius[i][j - 1] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
                elif j > 0 and i < len(field) - 1 and radius[i + 1][j - 1] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
                elif i < len(field) - 1 and radius[i + 1][j] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
                elif i < len(field) - 1 and j < len(field[0]) - 1 and radius[i + 1][j + 1] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
                elif j < len(field[0]) - 1 and radius[i][j + 1] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
                elif i > 0 and j < len(field[0]) - 1 and radius[i - 1][j + 1] == cl:
                    radius[i][j] = cl + 1
                    cnt += 1
        colors[cl + 1] = cnt
        cl += 1
        cnt = 0
    return radius, colors


def random_shape(board, direction, row, col):
    shapes = [[[1, 1, 1], [1, 0, 0]], [[1, 1, 1, 1]], [[0, 1, 0], [1, 1, 1]], [[0, 1, 1], [1, 1, 0]], [[1, 1], [1, 1]],
              [[1, 1, 1], [0, 0, 1]]]
    struct = choice(shapes)
    if direction in (0, 3):
        return Shape(struct, random_color(), (min(row, board.height - len(struct)), min(col, board.width - len(struct[0]))),
                 direction, board)
    else:
        return Shape(struct, random_color(),
                     (row, col),
                     direction, board)


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)
