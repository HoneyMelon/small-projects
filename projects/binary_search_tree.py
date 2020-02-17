from binary_node import Node


class BinarySearchTree:
    def __init__(self, value, left=None, right=None):
        self.root = Node(value, left, right)

    def insert(self, value):
        temp_node = self.root
        while True:
            # left side
            if value < temp_node.get_value():
                if temp_node.get_left() is None:
                    temp_node.set_left(Node(value))
                    return
                else:
                    temp_node = temp_node.get_left()
            # right side
            else:
                if temp_node.get_right() is None:
                    temp_node.set_right(Node(value))
                    return
                else:
                    temp_node = temp_node.get_right()

    def print_tree(self, space):
        self.print(self.root, space)

    def print(self, root, space):
        if root is None:
            return
        count = [10]
        space += count[0]

        self.print(root.get_right(), space)

        print()
        for i in range(count[0], space):
            print(end=" ")
        print(root.get_value())

        self.print(root.get_left(), space)


def main():
    test_tree = BinarySearchTree(10, Node(9, Node(8)), Node(19))
    test_tree.insert(5)
    test_tree.print_tree(3)

    test_tree.insert(7)

    test_tree.print_tree(3)


if __name__ == '__main__':
    main()
