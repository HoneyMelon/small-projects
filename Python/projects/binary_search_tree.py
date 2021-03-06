from binary_node import Node


class BinarySearchTree:
    def __init__(self, value, left=None, right=None):
        self.root = Node(value, left, right)

    def insert(self, new_node):
        """
        @param new_node: node type
        """

        while True:
            # left side
            if new_node.get_value() < self.root.get_value():
                if self.root.get_left() is None:
                    self.root.set_left(new_node)
                    return
                else:
                    self.root = self.root.get_left()
            # right side
            else:
                if self.root.get_right() is None:
                    self.root.set_right(new_node)
                    return
                else:
                    self.root = self.root.get_right()

    def _recursive_insert(self, root, new_node):
        """
        @param root: node type
        @param new_node: node type
        """
        # right side
        if root.get_value() < new_node.get_value():
            if root.get_right() is None:
                root.set_right(new_node)
            else:
                self._recursive_insert(root.get_right(), new_node)
        # left side
        else:
            if root.get_left() is None:
                root.set_left(new_node)
            else:
                self._recursive_insert(root.get_left(), new_node)

    def rec_insert(self, new_node):
        self._recursive_insert(self.root, new_node)

    def _find(self, root, node):
        """
        @param root: node type
        @param node: node type
        @return: node type
        """
        if root is None or root.get_value() is node.get_value():
            return root
        if root.get_value() < node.get_value():
            return self._find(root.get_right(), node)
        else:
            return self._find(root.get_left(), node)

    def find(self, node):
        return self._find(self.root, node)

    def min_node(self, root):
        """
        @return: node type
        """
        if root.get_left() is None:
            return root
        return self.min_node(root.get_left())

    def _delete(self, root, node):
        """
        @param node: node type
        """
        if root is None:
            return root

        if node.value < root.value:
            root.left = self._delete(root.left, node)
        elif node.value > root.value:
            root.right = self._delete(root.right, node)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self.min_node(root.right)
            root.value = min_node
            root.right = self._delete(root.right, root.value)
        return root

    def delete(self, node):
        return self._delete(self.root, node)

    def print_tree(self, space):
        print()
        print()
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
    test_tree.rec_insert(Node(20))
    # test_tree.print_tree(1)

    test_tree.rec_insert(Node(17))

    test_tree.print_tree(1)
    test_tree.delete(Node(10))
    test_tree.print_tree(1)


if __name__ == '__main__':
    main()
