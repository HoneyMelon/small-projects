# module for working with arrays
import copy
import random


def init_1d_list(number_of_elements, start=0):
    """
    @param number_of_elements: how many elements in list
    @param start: startvalue for element. 0 by default
    @return: 1d list
    """
    array = [start] * number_of_elements
    return array


def init_2d_list(row, column, start=0):
    """
    @param row: how many rows
    @param column: how many columns
    @param start: startvalue for element. 0 by default
    @return: 2d list
    """
    array_1d = init_1d_list(column, start)
    array = []
    for i in range(row):
        array.append(copy.deepcopy(array_1d))
    return array


def shuffle_list(array):
    """
    @param array: list
    @return: list with shuffled elements
    """
    random.shuffle(array)


def deep_shuffle_list(array):
    """
    @param array: list
    @return: new list with shuffled elements
    """
    copied_list = copy.deepcopy(array)
    random.shuffle(copied_list)
    return copied_list


def transpose_matrix(matrix):
    """
    @param matrix: 2d list
    @return: transposed matrix
    """
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    newMatrix = init_2d_list(columnCount, rowCount)
    for row in range(len(matrix)):
        for elem in range(len(matrix[row])):
            newMatrix[elem][row] = matrix[row][elem]
    return newMatrix


def _test_init_1d_list():
    test_array = [1, 1, 1, 1, 1]
    result = init_1d_list(5, 1)
    assert test_array == result


def _test_init_2d_list():
    matrix = [[1, 1, 1], [1, 1, 1]]
    result = init_2d_list(2, 3, 1)
    assert matrix == result
    result[0][0] = 5
    matrix[0][0] = 5
    assert matrix == result


def _test_shuffle_list():
    test_array = [1, 2, 3, 4, 5]
    result = [1, 2, 3, 4, 5]
    shuffle_list(result)
    for elem in test_array:
        assert elem in result


def _test_deep_shuffle_list():
    test_array = [1, 2, 3, 4, 5]
    result = deep_shuffle_list(test_array)
    for elem in test_array:
        assert elem in result


def _test_transpose_matrix():
    test_matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    result = transpose_matrix(test_matrix)
    assert result == expected


def main():
    try:
        _test_init_1d_list()
        _test_init_2d_list()
        _test_shuffle_list()
        _test_deep_shuffle_list()
        _test_transpose_matrix()
        print('Test successful')
    except AssertionError:
        print('Test failed')


if __name__ == '__main__':
    main()
