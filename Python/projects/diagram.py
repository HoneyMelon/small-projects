# module for creating diagrams
import math
import random
import stddraw
import color


def _get_min_max_for_one_dataset(array):
    """
    @param array: 2d Array
    @return: min and max values for x and y
    Calulates min and max for an array with one dataset of points
    """
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for point in array:
        newX = point[0]
        newY = point[1]
        minX = newX if newX < minX else minX
        maxX = newX if newX > maxX else maxX
        minY = newY if newY < minY else minY
        maxY = newY if newY > maxY else maxY

    return minX, maxX, minY, maxY


def _get_min_max_for_multiple_datasets(arrays):
    """
    @param arrays: 3d Array
    @return: min and max values for x and y
    Calculates min and max values for an array with multiple datasets of points
    """
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    for array in arrays:
        newMinX, newMaxX, newMinY, newMaxY = _get_min_max_for_one_dataset(array)
        minX = newMinX if newMinX < minX else minX
        maxX = newMaxX if newMaxX > maxX else maxX
        minY = newMinY if newMinY < minY else minY
        maxY = newMaxY if newMaxY > maxY else maxY

    return minX, maxX, minY, maxY


def _init_canvas(minX, maxX, minY, maxY):
    """
    @param minX: smallest x value
    @param maxX: largest x value
    @param minY: smallest y value
    @param maxY: largest y value
    Initialises a canvas with given scale
    """
    stddraw.clear(color.DARK_GRAY)
    stddraw.setXscale(minX - 1, maxX + 1)  # -4 bis 3
    stddraw.setYscale(minY - 1, maxY + 1)  # -1 bis 8


def _draw_coordinate_system(minX, maxX, minY, maxY):
    """
    @param minX: smallest x value
    @param maxX: largest x value
    @param minY: smallest y value
    @param maxY: largest y value
    Draws axis and numbers them
    """
    stddraw.setPenColor(color.WHITE)
    stddraw.setPenRadius(0.01)
    stddraw.line(minX - 1, 0, maxX + 1, 0)
    stddraw.line(0, minY - 1, 0, maxY + 1)

    for x in range(minX, maxX + 1):
        if not x == 0:
            stddraw.text(x, -0.5, str(x))

    for y in range(minY, maxY + 1):
        if not y == 0:
            stddraw.text(-0.2, y, str(y))


def _draw_points(array, pointcolor):
    """
    @param array: Array with points
    @param pointcolor: Color of points
    Draws given points in a color (TO BE USED FOR draw_data_random() FUNCTION)
    """
    stddraw.setPenColor(pointcolor)
    for point in array:
        stddraw.point(point[0], point[1])


def _draw_lines(array, linecolor):
    """
    @param array: Array with points
    @param linecolor: Color of points
    Draws points in given color,
    sorts them by their x value from smallest to largest and connects
    them with a line (TO BE USED FOR draw_data_random() FUNCTION)
    """
    stddraw.setPenColor(linecolor)
    array = sorted(array, key=lambda point: point[0])
    for i in range(len(array) - 1):
        stddraw.line(array[i][0], array[i][1], array[i+1][0], array[i+1][1])


def _draw_bars(array, barcolor):
    """
    @param array: Array with points
    @param barcolor: Color of bars
    Draws a rectangle in a given color with a width of 0.6 from the x axis
    to a given point (TO BE USED FOR draw_data_random() FUNCTION)
    """
    stddraw.setPenColor(barcolor)
    for point in array:
        yStart = 0 if point[1] > 0 else point[1]    # Bar starts at y=0 if y is positive and at y if y is negative
        stddraw.filledRectangle(point[0] - 0.3, yStart, 0.6, abs(point[1]))


def draw_data_random(data):
    """
    @param data: Array with multiple datasets of points
    Takes points from one dataset, randomly chooses one of the
    three methods (points, line, bars) and draws data them in a random color
    into coordinate system. Repeat for all datasets
    """
    minX, maxX, minY, maxY = _get_min_max_for_multiple_datasets(data)
    _init_canvas(minX, maxX, minY, maxY)

    for array in data:
        randomMethod = random.randint(0, 2)
        colors = [color.RED, color.ORANGE, color.YELLOW, color.GREEN, color.BLUE, color.CYAN,
                  color.MAGENTA, color.PINK, color.BOOK_LIGHT_BLUE, color.BOOK_RED]
        randomColor = colors[random.randint(0, len(colors) - 1)]
        if randomMethod == 0:
            _draw_points(array, randomColor)
        elif randomMethod == 1:
            _draw_lines(array, randomColor)
        else:
            _draw_bars(array, randomColor)

    _draw_coordinate_system(minX, maxX, minY, maxY)
    stddraw.show()


def draw_points(array, pointcolor=color.WHITE):
    """
    @param array: Array with points
    @param pointcolor: Color of points
    Draws the points into a coordinate system
    """
    minX, maxX, minY, maxY = _get_min_max_for_one_dataset(array)
    _init_canvas(minX, maxX, minY, maxY)
    _draw_points(array, pointcolor)
    _draw_coordinate_system(minX, maxX, minY, maxY)
    stddraw.show()


def draw_lines(array, linecolor=color.WHITE):
    """
    @param array: Array with points
    @param linecolor: Color of lines
    Draws points connected by lines into a coordinate system
    """
    minX, maxX, minY, maxY = _get_min_max_for_one_dataset(array)
    _init_canvas(minX, maxX, minY, maxY)
    _draw_lines(array, linecolor)
    _draw_coordinate_system(minX, maxX, minY, maxY)
    stddraw.show()


def draw_bars(array, barcolor=color.WHITE):
    """
    @param array: Array with points
    @param barcolor: Color of bars
    Draws bars into coordinate systems
    """
    minX, maxX, minY, maxY = _get_min_max_for_one_dataset(array)
    _init_canvas(minX, maxX, minY, maxY)
    _draw_bars(array, barcolor)
    _draw_coordinate_system(minX, maxX, minY, maxY)
    stddraw.show()


def _get_circle_coordinates(procent):
    """
    @param procent: given percents
    @return: x and y coordinates of points
    Calculates the x and y coordinates of the points on the border of our circle
    """
    radian = 2 * math.pi * procent / 100.0
    x = math.cos(radian)
    y = math.sin(radian)
    return x, y


def pie_diagram(probabilities):
    """
    @param probabilities: Array with probabilities
    Checks if the sum of the probabilities equals 100, initialises a background, draws one pie segment for each
    probability in a different color. Displaces the probabilities of each slice outside of the chart.
    """
    probability_sum = 0
    for probability in probabilities:
        probability_sum += probability
    if probability_sum != 100:
        print('Sum of probabilities is not 100')
        return
    stddraw.setXscale(-1.5, 1.5)
    stddraw.setYscale(-1.5, 1.5)
    stddraw.clear(color.DARK_GRAY)

    counter = 0
    colors = [color.RED, color.ORANGE, color.YELLOW, color.GREEN, color.BLUE, color.CYAN,
              color.MAGENTA, color.PINK, color.BOOK_LIGHT_BLUE, color.BOOK_RED]

    for probCount in range(len(probabilities)):
        probability = probabilities[probCount]
        pointsX = [0]
        pointsY = [0]
        for i in range(0, probability + 1):
            x, y = _get_circle_coordinates(counter)
            pointsX.append(x)
            pointsY.append(y)
            counter += 1
        counter -= 1 # Start the next pie segment on the same point where the last ended
        # draw text
        x, y = _get_circle_coordinates(counter - probability / 2.0)
        x *= 1.1
        y *= 1.1
        stddraw.setPenColor(colors[probCount % 10])
        stddraw.text(x, y, f'{probability}%')
        stddraw.filledPolygon(pointsX, pointsY)

    stddraw.show()


def _test_get_min_max_for_one_dataset():
    testdata = [1, 2], [2, 5], [-2, 7], [-3, 5], [5, -4]
    expected = -3, 5, -4, 7
    result = _get_min_max_for_one_dataset(testdata)
    assert result == expected


def _test_get_min_max_for_multiple_datasets():
    testdata = [
    [[1, 2], [2, 5], [-2, 7], [-3, 5], [5, -4]],
    [[1, 6], [0, 4], [-2, 1], [3, 1], [5, -8]],
    [[4, 2], [2, -2], [0, 2], [-2, 9], [-3, -4]]
    ]
    expected = -3, 5, -8, 9
    result = _get_min_max_for_multiple_datasets(testdata)
    assert result == expected


def main():
    try:
        _test_get_min_max_for_one_dataset()
        _test_get_min_max_for_multiple_datasets()
        print('\nTest bestanden')
    except AssertionError:
        print('\nFehler beim Test')


if __name__ == '__main__':
    main()


# pie_diagram([8, 7, 15, 10, 8, 10, 7, 9, 14, 4, 5, 3])
# draw_data_random(data)
# draw_lines(data[1], color.CYAN)