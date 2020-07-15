from typing import List, Tuple


class GroupMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self._total = {0: 0, 1: 0}
        self._search_for_uncheckeds_coordinates = [
            lambda x, y, array, element, index_checked: (x, y + 1)
            if y + 1 < len(array)
            and element == self.matrix[x][y + 1]
            and [x, y + 1] not in index_checked
            else (x, y),

            lambda x, y, array, element, index_checked: (x + 1, y)
            if x + 1 < len(self.matrix)
            and element == self.matrix[x + 1][y]
            and [x + 1, y] not in index_checked
            else (x, y),

            lambda x, y, array, element, index_checked: (x, y - 1)
            if y - 1 >= 0
            and element == self.matrix[x][y - 1]
            and [x, y - 1] not in index_checked
            else (x, y),

            lambda x, y, array, element, index_checked: (x - 1, y)
            if x - 1 >= 0
            and element == self.matrix[x - 1][y]
            and [x - 1, y] not in index_checked
            else (x, y),
        ]

    def _get_new_coordinates(self, x: int, y: int, array: List, element: int) -> Tuple[int, int, bool]:
        changed_coordinates = False
        new_x = x
        new_y = y
        for f in self._search_for_uncheckeds_coordinates:
            new_x, new_y = f(x, y, array, element, self._index_checked)
            if x != new_x or y != new_y:
                changed_coordinates = True
                break
        return new_x, new_y, changed_coordinates

    def _calculate_total_by_element(self, x: int, y: int, array: List, element: int):
        tx = []
        ty = []
        continue_while_main = True
        while continue_while_main:
            self._index_checked.append([x, y])
            tx.append(x)
            ty.append(y)
            try:
                x, y, _ = self._get_new_coordinates(x, y, array, element)
                tx.reverse()
                ty.reverse()
                pos = 0
                continue_while_trail = True
                while continue_while_trail:
                    try:
                        x, y, changed_coordinates = self._get_new_coordinates(
                            tx[pos], ty[pos], array, element
                        )
                        continue_while_trail = not changed_coordinates
                        pos += 1
                    except IndexError:
                        self._total[element] += 1
                        continue_while_main = False
                        break
            except IndexError:
                self._total[element] += 1
                break

    def get_grouping_of_elements(self) -> List[int]:
        self._index_checked = []
        for index_matrix, array in enumerate(self.matrix):
            for index_array, element in enumerate(array):
                x = index_matrix
                y = index_array
                if [x, y] not in self._index_checked:
                    self._calculate_total_by_element(x, y, array, element)

        return [self._total[1], self._total[0]]


if __name__ == "__main__":
    input_matrix = [
        [1, 0, 1, 1], 
        [1, 1, 1, 0], 
        [0, 1, 1, 0], 
        [0, 0, 0, 0]
    ]
    matrix = GroupMatrix(input_matrix)
    groups = matrix.get_grouping_of_elements()
    print(groups)
