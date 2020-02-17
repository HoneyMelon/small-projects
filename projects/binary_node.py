class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_value(self, value):
        self.value = value

    def set_left(self, value):
        self.left = value

    def set_right(self, value):
        self.right = value

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False


def main():
    test_node = Node(5)
    print('Node:', test_node)


if __name__ == '__main__':
    main()
