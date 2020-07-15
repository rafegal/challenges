from typing import List


class Matrix:
    def __init__(self, matrix: List[List]):
        self.matrix = matrix

    def groups_validation(self) -> List:
        total = {0: 0, 1: 0}
        index_checked = []
        for index_matrix, array in enumerate(self.matrix):
            for index_array, element in enumerate(array):
                x = index_matrix
                y = index_array
                tx = []
                ty = []
                if [x, y] not in index_checked:
                    continue_while_main = True
                    while continue_while_main:
                        index_checked.append([x, y])
                        tx.append(x)
                        ty.append(y)
                        try:
                            if (
                                y + 1 < len(array)
                                and element == self.matrix[x][y + 1]
                                and [x, y + 1] not in index_checked
                            ):
                                y += 1
                            elif (
                                x + 1 < len(self.matrix)
                                and element == self.matrix[x + 1][y]
                                and [x + 1, y] not in index_checked
                            ):
                                x += 1
                            elif (
                                y - 1 >= 0
                                and element == self.matrix[x][y - 1]
                                and [x, y - 1] not in index_checked
                            ):
                                y -= 1
                            elif (
                                x - 1 >= 0
                                and element == self.matrix[x - 1][y]
                                and [x - 1, y] not in index_checked
                            ):
                                x -= 1
                            else:
                                tx.reverse()
                                ty.reverse()
                                pos = 0
                                while True:
                                    try:
                                        nx = tx[pos]
                                        ny = ty[pos]
                                        if (
                                            ny + 1 < len(array)
                                            and element == self.matrix[nx][ny + 1]
                                            and [nx, ny + 1] not in index_checked
                                        ):
                                            y = ny + 1
                                            x = nx
                                            break
                                        elif (
                                            nx + 1 < len(self.matrix)
                                            and element == self.matrix[nx + 1][ny]
                                            and [nx + 1, ny] not in index_checked
                                        ):
                                            x = nx + 1
                                            y = ny
                                            break
                                        elif (
                                            ny - 1 >= 0
                                            and element == self.matrix[nx][ny - 1]
                                            and [nx, ny - 1] not in index_checked
                                        ):
                                            y = ny - 1
                                            x = nx
                                            break
                                        elif (
                                            nx - 1 >= 0
                                            and element == self.matrix[nx - 1][ny]
                                            and [nx - 1, ny] not in index_checked
                                        ):
                                            x = nx - 1
                                            y = ny
                                            break
                                        pos += 1
                                    except IndexError:
                                        total[element] += 1
                                        continue_while_main = False
                                        break
                        except IndexError:
                            total[element] += 1
                            break
        return [total[1], total[0]]


if __name__ == "__main__":
    input_matrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1]
    ]
    matrix = Matrix(input_matrix)
    groups = matrix.groups_validation()
    print(groups)